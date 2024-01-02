from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from redis_om import get_redis_connection, HashModel
from pydantic import BaseModel
from dotenv import load_dotenv
import os

app = FastAPI()

load_dotenv()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000', 'http://localhost:8001'],
    allow_methods=['*'],
    allow_headers=['*']
)

host = os.getenv('host')
port = os.getenv('port')
password = os.getenv('password')

redis = get_redis_connection(
    host=host,
    port=port,
    password=password,
    decode_responses=True
)

class Product(HashModel):
    name: str
    price: float
    quantity: int

    class Meta:
        database = redis

class ProductRequest(BaseModel):
    name: str
    price: float
    quantity: int


@app.get('/products', response_model=list)
def products():
    try:
        return [format(pk) for pk in Product.all_pks()]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
def format(pk: str):
    product = Product.get(pk)

    return {
        'id': product.pk,
        'name': product.name,
        'price': product.price,
        'quantity': product.quantity
    }


@app.post('/products')
def create(product_req: ProductRequest):
    try:
        product = Product(**product_req.model_dump())
        return product.save()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get('/products/{pk}')
def get(pk: str):
    return Product.get(pk)

@app.delete('/products/{pk}')
def delete(pk: str):
    return Product.delete(pk)