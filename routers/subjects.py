from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.connection import get_db
from database.model import Subject
from schemas.scheme import SubjectOut
from security.auth import is_admin
router = APIRouter(
    prefix="/subjects",
    tags=["subject"]
)

@router.get("/", response_model=list[SubjectOut])
def get_all_subjects(db: Session = Depends(get_db)):
    subjects = db.query(Subject).all()
    return subjects

@router.get("/subjects/{id}", response_model=SubjectOut)
def get_subject(id: int, db: Session = Depends(get_db), admin_user: dict = Depends(is_admin)):
    subject = db.query(Subject).filter(Subject.id == id).first()
    if not subject:
        raise HTTPException(status_code=404, detail="Subject no encontrado")
    return subject


