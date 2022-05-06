from cgitb import reset
from urllib import response
from flask import Blueprint, request
from function_jwt import validate_token
test_service = Blueprint("test_service", __name__)


@test_service.before_request
def verify_token_middleware():
    token = request.headers['Authorization'].split(" ")[1]
    return validate_token(token,output=False)

@test_service.route("/test", methods=["POST"])
def testservice():
    data = request.get_json()
    nombre = data['nombre']
    return f'hola {nombre}!'


