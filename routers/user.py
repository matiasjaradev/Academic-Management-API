from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from passlib.context import CryptContext

from database import model
from schemas import scheme
from security.auth import create_access_token
from database.connection import get_db
from sqlalchemy import func


router = APIRouter(
    prefix="",
    tags=["Authentication"]
)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

@router.post("/register", response_model=scheme.User)
def register(user_create: scheme.UserCreate, db: Session = Depends(get_db)):
    user = db.query(model.User).filter(model.User.username == user_create.username).first()
   
    if user:
        raise HTTPException(status_code=400, detail="El usuario ya existe")

    role = db.query(model.Role).filter(model.Role.name == "user").first()
    if not role:
        raise HTTPException(status_code=400, detail="Rol 'user' no encontrado")

    new_user = model.User(
        username=user_create.username,
        hashed_password=get_password_hash(user_create.password),
        role_id=1
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@router.post("/login", response_model=scheme.Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(model.User).filter(model.User.username == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Usuario o contraseña incorrectos")

    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}