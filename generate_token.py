import jwt
from datetime import datetime, timedelta, timezone

def gerar_token(id_usuario):
    payload = {
        "id_usuario": id_usuario,
        "exp": datetime.now(timezone.utc) + timedelta(hours=1)
    }
    token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')
    return token