# Movie & Show Ratings API

## Setup

```bash
pip install -r requirements.txt
cp .env .env  # edit SECRET_KEY if needed
```

## Run

```bash
uvicorn app.main:app --reload
```

Docs: http://localhost:8000/docs

## Endpoints

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| POST | /users/register | No | Register user |
| POST | /users/login | No | Login, get JWT |
| GET | /users/me | Yes | Current user |
| POST | /titles/ | No | Create title |
| GET | /titles/ | No | List titles |
| GET | /titles/{id} | No | Get title |
| DELETE | /titles/{id} | No | Delete title |
| POST | /reviews/ | Yes | Create review |
