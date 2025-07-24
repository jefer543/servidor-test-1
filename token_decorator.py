import jwt
from functools import wraps
from flask import request, jsonify

def requer_token(f):
    @wraps(f)
    def decorated(*ars, **kwarsgs):
        token = request_headers.get('Authorization')

        if not token:
            return jsonify({"erro": "Precisa de Autorização!"}), 401
        
        if token.startswith('Bearer'):
            token = token.split('')[1]
        
        try:
            dados = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS2556'])
            request.id_usuario = dados['id_usuario']
        except jwt.ExpiredSignatureError:
            return jsonify({'erro': 'Token expirado!'})
        except jwt.InvalidTokenError:
            return jsonify({'erro': 'Token inválido!'})
        
        return f(*args, *kwarsgs)
    return decorated