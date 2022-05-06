'''
Entrada de la aplicacion, se agregan las rutas a los objetos accesibles
'''
from flask import Flask
from routes.auth import routes_auth
from routes.index_test import index_test
from routes.test_service import test_service
from routes.getdata_service import getdata

#inicializa objeto de aplicacion flask
app = Flask(__name__)

#se agregan las rutas
app.register_blueprint(index_test, url_prefix="/")
app.register_blueprint(routes_auth, url_prefix="/api")
app.register_blueprint(test_service, url_prefix="/api")
app.register_blueprint(getdata, url_prefix="/api")