'''
conexion a base de datos
'''
import pyodbc
import os


def get_context():
    '''
    regresa una conexion establecida a la base
    '''
    dnsname = os.environ['DNS_DB']
    context = pyodbc.connect("DSN=" + dnsname,autocommit=True)
    return context
