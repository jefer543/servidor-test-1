import os
import jwt
from functools import wraps
from flask import request, jsonify

def requer_token(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')

        if not token:
            return jsonify({"erro": "Precisa de Autorização!"}), 401
        
        if token.startswith('Bearer '):
            token = token.split(' ')[1]
            print(token)
        
        try:
            dados = jwt.decode(token, os.getenv('SECRET_KEY'), algorithms=['HS256'])
            print(dados)
            request.id_usuario = dados['id_usuario']
        except jwt.ExpiredSignatureError:
            return jsonify({'erro': 'Token expirado!'})
        except jwt.InvalidTokenError:
            return jsonify({'erro': 'Token inválido!'})
        
        return f(*args, **kwargs)
    return decorated