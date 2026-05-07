from pydantic import BaseModel, EmailStr
from typing import Optional
from app.models import TitleType


# ───────────────────────────────
# USER SCHEMAS
# ───────────────────────────────

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        from_attributes = True


# ───────────────────────────────
# TOKEN SCHEMA
# ───────────────────────────────

class Token(BaseModel):
    access_token: str
    token_type: str


# ───────────────────────────────
# TITLE SCHEMAS
# ───────────────────────────────

class TitleCreate(BaseModel):
    name: str
    type: TitleType
    year: int


class TitleOut(BaseModel):
    id: int
    name: str
    type: TitleType
    year: int

    class Config:
        from_attributes = True


# ───────────────────────────────
# REVIEW SCHEMAS
# ───────────────────────────────

class ReviewCreate(BaseModel):
    rating: int
    text: Optional[str] = None
    title_id: int


class ReviewOut(BaseModel):
    id: int
    rating: int
    text: Optional[str] = None
    user_id: int
    title_id: int

    class Config:
        from_attributes = True