from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database.connection import Base

class Role(Base):
    __tablename__ = "roles"
    __table_args__ = {'schema': 'ubo_api'}

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)

class User(Base):
    __tablename__ = "users"
    __table_args__ = {'schema': 'ubo_api'}

    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role_id = Column(Integer, ForeignKey("ubo_api.roles.id"))
    role = relationship("Role")

class Subject(Base):
    __tablename__ = "subjects"
    __table_args__ = {'schema': 'ubo_api'}
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)


class Student(Base):
    __tablename__ = "students"  # corregido de "studients"
    __table_args__ = {'schema': 'ubo_api'}
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    subject_id = Column(Integer, ForeignKey("ubo_api.subjects.id"))  # corregido de "asignaturas.id"

    subject = relationship("Subject")
