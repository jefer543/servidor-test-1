import os
from dotenv import load_dotenv
import jwt
from datetime import datetime, timedelta, timezone

load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')

def gerar_token(id_usuario):
    payload = {
        "id_usuario": id_usuario,
        "exp": datetime.now(timezone.utc) + timedelta(hours=1)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token