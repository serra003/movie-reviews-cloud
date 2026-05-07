from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app import crud, schemas
from app.dependencies import get_current_user

router = APIRouter(prefix="/reviews", tags=["Reviews"])


# ───────────────────────────────
# CREATE REVIEW (AUTH REQUIRED)
# ───────────────────────────────

@router.post("/", response_model=schemas.ReviewOut)
def create_review(
    review: schemas.ReviewCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return crud.create_review(db, review, current_user.id)


# ───────────────────────────────
# GET ALL REVIEWS
# ───────────────────────────────

@router.get("/", response_model=list[schemas.ReviewOut])
def get_all_reviews(db: Session = Depends(get_db)):
    return crud.get_all_reviews(db)


# ───────────────────────────────
# GET REVIEWS BY TITLE ID
# ───────────────────────────────

@router.get("/title/{title_id}", response_model=list[schemas.ReviewOut])
def get_reviews_by_title(title_id: int, db: Session = Depends(get_db)):
    return crud.get_reviews_by_title(db, title_id)