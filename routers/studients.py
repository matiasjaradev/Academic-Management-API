from fastapi import APIRouter, Depends
from database.model import Student
from database.connection import get_db
from schemas.scheme import studientsOut, studientsOutCategories, studientsIn
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
from typing import List
from security.auth import is_admin
from sqlalchemy import func
router = APIRouter(    
    prefix="/studients",
    tags=["studients"]
)

@router.get("/", response_model=List[studientsOut])
def get_all_students(db: Session = Depends(get_db)):
     return db.query(Student).all()
    
@router.get("/subject_id", response_model=List[studientsOutCategories])
def get_students_categories(subject_id: str,db: Session = Depends(get_db)):
     students = db.query(Student).filter(Student.subject_id == subject_id).all()
     if not students:
      raise HTTPException(status_code=404, detail='Recurso no existe') 
     return students

@router.get("/{id}", response_model=studientsOut)
def get_studient_id(id: int, db: Session = Depends(get_db)):
     student = db.query(Student).filter(Student.id == id).first()
     if not student:
      raise HTTPException(status_code=404, detail={'code': '404','message':'Recurso no existe'}) 
     return student 


@router.post("/", response_model=studientsIn)
def create_studient(
    studient: studientsIn,
    db: Session = Depends(get_db),
    admin_user: dict = Depends(is_admin) 
):
    max_id = db.query(func.max(Student.id)).scalar()
    new_id = (max_id or 0) + 1 
    new_student = Student(id=new_id,**studient.dict())
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student


@router.put("/{id}", response_model=studientsOut)
def update_studient(
    id: int,
    studient_update: studientsIn,
    db: Session = Depends(get_db),
    admin_user = Depends(is_admin)
):
    student = db.query(Student).filter(Student.id == id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")

    # Actualizar los campos permitidos
    for key, value in studient_update.dict(exclude_unset=True).items():
        setattr(student, key, value)

    db.commit()
    db.refresh(student)
    return student

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_studient(
    id: int,
    db: Session = Depends(get_db),
    admin_user = Depends(is_admin)
):
    student = db.query(Student).filter(Student.id == id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")

    db.delete(student)
    db.commit()
    return JSONResponse(status_code=status.HTTP_204_NO_CONTENT, content=None)
