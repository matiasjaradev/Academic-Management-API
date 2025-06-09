from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session 

from database import model 
from schemas import scheme
from security.auth import get_current_user, is_admin
from database.connection import get_db

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get("/me", response_model=scheme.User)
def read_current_user(
    current_user: model.User = Depends(get_current_user)
):
    return current_user

# Ruta solo accesible para administradores
@router.get("/admin-only", response_model=scheme.User)
def admin_route(
    current_user: model.User = Depends(is_admin)
):
    return current_user