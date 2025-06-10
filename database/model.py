from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database.connection import Base

class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)

class User(Base):
    __tablename__ = "users"

    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role_id = Column(Integer, ForeignKey("roles.id"))
    role = relationship("Role")

class Subject(Base):
    __tablename__ = "subjects"
    
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)


class Student(Base):
    __tablename__ = "students"  # corregido de "studients"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    subject_id = Column(Integer, ForeignKey("subjects.id"))  # corregido de "asignaturas.id"

    subject = relationship("Subject")
