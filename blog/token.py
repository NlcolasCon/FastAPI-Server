from typing import Optional
from datetime import timedelta, datetime
from jose import JWTError, jwt
from fastapi import HTTPException   
from . import schemas

SECRET_KEY = "7fffc6e87b2ceb9c81e6af90c5bfe9bffb8c0ac231064065ab33787a4e15681d"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm = ALGORITHM)
    return encoded_jwt

def verify_token(token_input:str, credentials_exception):
    try:
        payload = jwt.decode(token_input, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = schemas.TokenData(username=email)
    except JWTError:
        raise credentials_exception
    return token_data