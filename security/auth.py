from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from jose import JWTError, jwt
from sqlalchemy.orm import Session
from database.connection import get_db
from database import model
from schemas import scheme
from dotenv import load_dotenv
import os
load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")



def create_access_token(data: dict):
    print("🛠 Datos codificados en JWT:", data)
    TOKEN = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
    print("token generado:", TOKEN)
    return TOKEN


def get_current_user(token: str  = Depends(oauth2_scheme), db: Session = Depends(get_db)):
     credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail={"message": "Credenciales invalidad"},
        headers={"WWW-Authenticate": "Bearer"}
    )
     try:
          payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
          username = payload.get("sub")
          if username is None:
               raise credentials_exception
     except JWTError as e:
        raise credentials_exception
     
     user = db.query(model.User).filter(model.User.username == username).first()
     if user is None:
         print(username)
         raise credentials_exception

     return user


def is_admin(user: scheme.User = Depends(get_current_user)):
    if user.role.name != "admin":
        raise HTTPException(status_code=403, detail="Acceso denegado")
    return user