import json
from decimal import Decimal
from flask import Response


# recorre una lista para serializar valores decimales y poder formar un json corercto
def default(obj):
	if isinstance(obj, Decimal):
		return float(obj)
	return str(obj)

# busca en un arreglo de scope los parametros de configuracion
def search(list, key):
	for i in range(len(list)):
		if list[i].split(':')[0] == key:
			return list[i].split(':')[1]
	return False

# regresa una respuesta del servicio
def respuesta(objeto):
	resp = Response(json.dumps(objeto, default=default))
	resp.headers["content-type"] = "application/json"
	return resp
