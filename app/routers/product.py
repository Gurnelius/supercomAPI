from fastapi import FastAPI, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from ..database import engine, get_db
from .. import models, schemas
from fastapi.routing import APIRouter
from typing import List

router = APIRouter()

# Get all products
@router.get('/products', response_model=List[schemas.ProductOut])
def get_all_products(db: Session = Depends(get_db)):
    products = db.query(models.Product).all()

    if products == None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f"Products not found.")
  
    return products

# Get one product
@router.get('/products/{id}', response_model=schemas.ProductOut)
def get_all_products(id: int, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id==id).first()

    if product == None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f"Product with id {id} not found.")
    return product

# Create a product
@router.post('/products', response_model = schemas.ProductOut)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    store_id = 1
    product = models.Product(store_id = store_id, **product.dict())
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

# Delete a product
@router.delete('/products/{id}')
def delete_product(id: int, db: Session = Depends(get_db)):
    query = db.query(models.Product).filter(models.Product.id == id)
    
    product = query.first()
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"Product with id {id} not found.")
    
    query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

# Update a product
@router.put('/products/{id}', response_model= schemas.ProductOut)
def update_product(id: int, product: schemas.ProductCreate, db: Session = Depends(get_db)):
    query = db.query(models.Product).filter(models.Product.id == id)

    update_product = query.first()

    if not update_product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Product with id {id} not found.")
    
    query.update(product.dict())
    db.commit()
    return query.first()