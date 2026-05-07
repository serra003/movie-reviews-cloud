from sqlalchemy.orm import Session
from app import models, schemas
from app.auth import hash_password


# ───────────────────────────────
# USERS
# ───────────────────────────────

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(
        username=user.username,
        email=user.email,
        hashed_password=hash_password(user.password)
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# ───────────────────────────────
# TITLES
# ───────────────────────────────

def create_title(db: Session, title: schemas.TitleCreate):
    db_title = models.Title(
        name=title.name,
        type=title.type,
        year=title.year
    )
    db.add(db_title)
    db.commit()
    db.refresh(db_title)
    return db_title


def get_titles(db: Session):
    return db.query(models.Title).all()


def get_title(db: Session, title_id: int):
    return db.query(models.Title).filter(models.Title.id == title_id).first()


def delete_title(db: Session, title_id: int):
    title = get_title(db, title_id)
    if title:
        db.delete(title)
        db.commit()
    return title


# ───────────────────────────────
# REVIEWS
# ───────────────────────────────

def create_review(db: Session, review: schemas.ReviewCreate, user_id: int):
    db_review = models.Review(
        rating=review.rating,
        text=review.text,
        user_id=user_id,
        title_id=review.title_id
    )
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review


def get_all_reviews(db: Session):
    return db.query(models.Review).all()


def get_reviews_by_title(db: Session, title_id: int):
    return db.query(models.Review).filter(
        models.Review.title_id == title_id
    ).all()