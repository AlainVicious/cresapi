'''
Servicio de consultas dinamicas
'''

from data import db
from models import ErrorResponse
from tools import search, respuesta
from flask import Blueprint, request
from function_jwt import validate_token

getdata = Blueprint("getmline", __name__)

# middleware para validar el token
@getdata.before_request
def verify_token_middleware():
    token = request.headers['Authorization'].split(" ")[1]
    token = validate_token(token,output=False)

@getdata.route("/<table>", methods=["GET"])
def getmlinem(table):
	'''
	ruta del servicio dinamico principal 
	recibe query string para parametrizacion:
		requerido en path:
			table: nombre de la tabla a consultar
				https://localhost/api/nombre_tabla

		opcional en querystring: (https://localhost/api/nombre_tabla?fields=nombre_columna_1,nombre_columna_2)
			fields(str): indica las columnas que queremos regresar en formato.
				fields=nombre_columna_1,nombre_columna_2,nombre_columna_3
			top(int): especificar el número de filas a mostrar en el resultado.
				top=10
			sort_key(str):nombre de la columna para ordenar
				sort_key=nombre_columna
			sort(str(default asc, opcional desc)):utiliza para ordenar los resultados de una consulta, según el valor de la columna especificada(sort_key).
				sort=desc
			key(str), value(str): filtra el contenido por un campo, se indica el nombre de columnay con value el valor deseado
				key=nombre_columna&value=valor_buscado
			strict(bool): si este se pone en false busca valores parecidos al indicado en value
				key=nombre_columna&value=valor_buscado&strict=false
			
	'''
	try :
		args = request.args
		token = request.headers['Authorization'].split(" ")[1]
		token = validate_token(token,output=False)

		if not token['scope']:
			return respuesta(ErrorResponse("no se encontro el scope en el token",'GDSP01')), 403
		directorio = search(token['scope'], 'dir')
		if not directorio:
			return respuesta(ErrorResponse("no se encontro el scope directorio en el token",'GDDR01')), 403
		empresa = search(token['scope'], 'emp')
		if not empresa:
			return respuesta(ErrorResponse("no se encontro el scope empresa en el token",'GDCS01')), 403

		if not request.view_args['table'] :
			return respuesta(ErrorResponse('no se especifico el campo ''table''', 'GDT01').__dict__), 400
		table = request.view_args['table']
		value = ''
		top = False
		fields = ''
		key = ''
		sort = ''
		sort_key = ''
		strict = 'true'
		if len(args) > 0:
			if args.get("top"):
				top = args.get("top")
			if args.get("fields"):
				fields = args.get("fields")
			if args.get("key"):
				key = args.get("key")
				if args.get("value"):
					value = args.get("value")
				else:
					return respuesta(ErrorResponse('se establecio un filtro pero no se esta indicando el valor', 'GDT01').__dict__), 400
			if args.get("strict"):
				strict = args.get("strict")
				if strict.lower() == 'false':
					strict = ''
			if args.get("sort"):
				sort = args.get("sort")
			if args.get("sort_key"):
				sort_key = args.get("sort_key")
				
		
		
		conn = db.get_context()
		if not conn:
			return respuesta(ErrorResponse('Error de conexion', 'GDC01').__dict__), 500
		else :
			# 					directorio\empresa
			# scope = ["dir:grupoxkaan", "emp:DEMO"]
			sql = "Select * from "+ directorio +"\\" + empresa + "\\" +table 
			if fields:
				sql = sql.replace('*', fields)
			if key :
				sql = sql + ' where ' + key
				if strict:
					sql += ' = \''+ value + '\'' 
				else:
					sql += ' like \'%'+ value + '%\'' 
			if top :
				sql = sql.replace('Select', 'Select top ' + top)
			if sort_key :
				sql = sql + ' order by ' + sort_key
				if sort == 'desc':
					sql += ' desc'
			
			cursor = conn.execute(sql)
			resultados = [dict(zip([column[0] for column in cursor.description], row))
				for row in cursor.fetchall()]
			objeto = {}
			objeto['resultados'] = len(resultados)
			objeto['items'] = resultados
			return respuesta(objeto)
	except Exception as e:
		return respuesta(ErrorResponse('Se presento un error no controlado, comunicar con soporte', 'GDEX01').__dict__), 500


