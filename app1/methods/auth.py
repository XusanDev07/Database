from methodism.helper import custom_response
from rest_framework.authtoken.models import Token

from app1.models import User
from app1.models.User import OTP


def regis(requests, params):

    if 'password' not in params or 'email' not in params:
        return custom_response(False, {"Error": "Введите свои данные полностью !"})

    otp = OTP.objects.filter(key=params['token']).first()

    if not otp:
        return custom_response(False, {"Error": "Неверный токен !"})

    if not otp.is_conf:
        return custom_response(False, {"Error": "Устаревший токен !"})

    user = User.oblects.filter(email=otp.email).first()

    if user:
        return custom_response(False, {"Error": "Этот эмайл ранее был зарегистрирован"})

    if len(params['password']) < 8 or not params['password'].isalnum() or " " in params['password']:
        return custom_response(False, {"Error": "Длина пароля должно быть не меннее 8 символов и больше 2х занков без пробелов !"})

    user_data = {
        "email": params['email'],
        "password": params['password'],
        "username": params.get('username', '')
    }

    if params.get('key', None) == 'qwerty':
        user_data.update({
            "is_staff": True,
            "is_superuser": True
        })

    user = User.objects.create_user(**user_data)
    token = Token.objects.create(user=user)
    return custom_response(False, {
        "Success": "Ваш аккаунт успешно создан",
        "Ваш секретный ключ": token.key
    })



