from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import  Optional

class ProductBase(BaseModel):
    name: str
    price: float

class Product(BaseModel):
    id: int
    created_at: datetime
    name: str
    price: float

class ProductCreate(ProductBase):
    pass


class ProductOut(Product):
    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: str
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True

        
class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


    class Config:
        orm_mode = True


class TokenData(BaseModel):
    id: Optional[str] = None