from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

Pro=[]
    
class Products(BaseModel):
    name: str
    id: int
    description: str
    price: int

        
@app.post("/products/")
def create_product(product: Products):
        Pro.append(product.dict())
        return{
            "msg":"Product added successfully",
            "data": Pro
        }



@app.get("/GetProduct/")
def get_product():
        return{
            "msg":"Product data recived sucssfully",
            "data":Pro
        }