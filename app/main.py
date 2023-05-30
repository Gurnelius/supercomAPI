from fastapi import FastAPI, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from .database import engine, get_db
from . import models, schemas
from .routers import product,user,order, auth

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get('/')
def root():
    return {"message": "Welcome to supercom API."}

app.include_router(product.router)
app.include_router(user.router)
app.include_router(auth.router)