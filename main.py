from flask import Flask
from routes.auth import routes_auth
from routes.test_service import test_service
from routes.getdata_service import getdata
from dotenv import load_dotenv

from OpenSSL import SSL
# context = SSL.Context(SSL.TLSv1_2_METHOD)
# context.use_privatekey_file('C:\\xampp\\apache\conf\ssl.key\server.key')
# context.use_certificate_file('C:\\xampp\\apache\conf\ssl.crt\server.crt') 
# context.set_cipher_list('HIGH:!DH:!aNULL:DEFAULT@SECLEVEL=1')
context=('C:\\xampp\\apache\\conf\\ssl.crt\\server.crt','C:\\xampp\\apache\\conf\\ssl.key\\server.key')
app = Flask(__name__)

app.register_blueprint(routes_auth, url_prefix="/api")
app.register_blueprint(test_service, url_prefix="/api")
app.register_blueprint(getdata, url_prefix="/api")


if __name__ == '__main__':
    load_dotenv()
    # app.run(debug=True, port="81", host="0.0.0.0")
from os import environ
if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '430'))
    except ValueError:
        PORT = 430
    app.run(HOST, PORT, ssl_context=context,threaded=True, debug=True)
    