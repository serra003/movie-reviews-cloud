from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app import crud, schemas
from app.dependencies import get_db

router = APIRouter(prefix="/titles", tags=["titles"])


# ✅ CREATE (BATCH FIXED)
@router.post("/", response_model=List[schemas.TitleOut], status_code=201)
def create_titles(
    data: List[schemas.TitleCreate],
    db: Session = Depends(get_db)
):
    return crud.create_titles(db, data)


# GET ALL
@router.get("/", response_model=List[schemas.TitleOut])
def list_titles(db: Session = Depends(get_db)):
    return crud.get_titles(db)


# GET ONE
@router.get("/{title_id}", response_model=schemas.TitleOut)
def get_title(title_id: int, db: Session = Depends(get_db)):
    title = crud.get_title(db, title_id)
    if not title:
        raise HTTPException(status_code=404, detail="Title not found")
    return title


# DELETE
@router.delete("/{title_id}", status_code=204)
def delete_title(title_id: int, db: Session = Depends(get_db)):
    title = crud.delete_title(db, title_id)
    if not title:
        raise HTTPException(status_code=404, detail="Title not found")