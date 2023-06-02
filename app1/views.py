from methodism import METHODISM, custom_response, error_messages, MESSAGE, code_decoder
from app1 import methods


class Main(METHODISM):
    file = methods
    not_auth_methods = ['regis']


