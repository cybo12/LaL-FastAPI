from typing import List

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse

import models
import schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

#app.add_middleware(
#    CORSMiddleware,
#    allow_origins=["*"],
#    allow_methods=["*"],
#    allow_headers=["*"],
#    allow_credentials=True,
#)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get("/")
def main():
    return { 'message': 'Bonjour Gologic' }


@app.get("/users/", response_model=List[schemas.User])
def get_all_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    new_user = models.User(name=user.name)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
