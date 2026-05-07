from sqlalchemy import Column, Integer, String, ForeignKey, Text, Enum
from sqlalchemy.orm import relationship
from app.database import Base
import enum

class TitleType(str, enum.Enum):
    movie = "movie"
    show = "show"

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    reviews = relationship("Review", back_populates="user")

class Title(Base):
    __tablename__ = "titles"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    type = Column(Enum(TitleType), nullable=False)
    year = Column(Integer, nullable=False)
    reviews = relationship("Review", back_populates="title")

class Review(Base):
    __tablename__ = "reviews"
    id = Column(Integer, primary_key=True, index=True)
    rating = Column(Integer, nullable=False)
    text = Column(Text)
    user_id = Column(Integer, ForeignKey("users.id"))
    title_id = Column(Integer, ForeignKey("titles.id"))
    user = relationship("User", back_populates="reviews")
    title = relationship("Title", back_populates="reviews")
