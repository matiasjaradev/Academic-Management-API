from pydantic import BaseModel
from typing import Optional

# ----------------------------------
# Esquemas de autenticación
# ----------------------------------

class UserCreate(BaseModel):
    username: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

# ----------------------------------
# Esquemas para el usuario y rol
# ----------------------------------

class Role(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

class User(BaseModel):
    id: int
    username: str
    role: Role  # Esto permite acceder a user.role.name

    class Config:
        from_attributes = True

class studientsOut(BaseModel):
    id: int
    name: str
    subject_id: int

    class Config:
        from_attributes  = True
class studientsOutCategories(BaseModel):
    id: int
    name: str

class studientsIn(BaseModel):
    name: str
    subject_id: int 
class SubjectOut(BaseModel):
    id: int
    name: str
    