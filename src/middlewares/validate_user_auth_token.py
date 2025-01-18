import os
import jwt
from fastapi import Request, Response, HTTPException

SECRET_KEY = os.getenv("SECRET_KEY", "sua_chave_secreta")  # Chave JWT
ALGORITHM = "HS256"

def validate_auth_token(request: Request):
    token = request.cookies.get("auth_token")  # Nome genérico para o cookie do token
    if not token:
        raise HTTPException(status_code=401, detail="Token não encontrado")

    try:
        # Decodifica o token JWT
        payload = jwt.decode(token.split(" ")[1], SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("id")
        if not user_id:
            raise HTTPException(status_code=401, detail="Token inválido")
        request.state.auth_payload = {"user_id": user_id}  # Armazena as informações do token no request

    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Token inválido")

    return True
