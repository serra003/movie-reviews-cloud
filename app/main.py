"""
main.py - Application entry point.
Creates the FastAPI app, registers routers, initialises the database,
and adds global error handling middleware for Movie & Show Ratings API.
"""

from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine
from app.routers import users, titles, reviews

# ─── Create database tables ───────────────────────────────────────────────────
Base.metadata.create_all(bind=engine)

# ─── FastAPI app instance ─────────────────────────────────────────────────────
app = FastAPI(
    title="Movie & Show Ratings API",
    description=(
        "A backend API for managing movies and TV shows, "
        "user reviews, and ratings with JWT authentication."
    ),
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# ─── CORS Middleware ──────────────────────────────────────────────────────────
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ─── Global Exception Handler ────────────────────────────────────────────────
@app.exception_handler(Exception)
async def generic_exception_handler(request: Request, exc: Exception):
    """
    Catches all unhandled errors and returns a clean JSON response.
    """
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "detail": "An internal server error occurred. Please try again later."
        },
    )

# ─── Routers ──────────────────────────────────────────────────────────────────
app.include_router(users.router)
app.include_router(titles.router)
app.include_router(reviews.router)

# ─── Health Check Endpoint ────────────────────────────────────────────────────
@app.get("/", tags=["Health"])
def root():
    return {
        "status": "ok",
        "message": "Movie & Show Ratings API is running"
    }