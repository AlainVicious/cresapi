'''
Inicializa la aplicacion por modulo wsgi de apache
'''
import sys, os
sys.path.insert(0, 'C:\\xampp\htdocs\ws\webservice')
# llave de encripcion de token
os.environ['SECRET'] = 'S3cr3tK3y'
# DNS de base de datos
os.environ['DNS_DB'] = 'Crescloud'
from webservice import app as application