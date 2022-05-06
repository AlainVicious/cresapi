from re import split
from flask import Blueprint, request, jsonify


index_test = Blueprint("index_test", __name__)


@index_test.route("")
def ind():
    return 'prueba entrega'

