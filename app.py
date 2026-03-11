from fastapi import FastAPI
from storage import load_products,save_products
from pydantic import BaseModel
class new_prdt(BaseModel):
    name:str
    price:float
    stock:int
    category:str
productapp=FastAPI()
products,nxt_prdt_no=load_products("product_data.json")
@productapp.get("/")
def home():
    return {"message":"Hi,Welcome to shop manager"}
@productapp.get("/viewproducts/{prdt_no}")
def view_product(prdt_no:int):
    if len(products)<=0:
        return{"error":"Create products first"}
    else:
        if prdt_no in products:
            return {"Product Details":products[prdt_no].to_dict()}
        else:
            return {"error":"Product not found"}
@productapp.get("/view_all_products")
def view_all_producs()->dict:
    if len(products)<=0:
        return{"error":"Create products first"}
    else:
        return{"products":{p_no:dtls.to_dict() for p_no,dtls in products.items()}}
@productapp.post("/add_product")
def add_product(n_prdt:new_prdt):
    global nxt_prdt_no
    from product import Product
    products[nxt_prdt_no]=Product(nxt_prdt_no,n_prdt.name,n_prdt.price,n_prdt.stock,n_prdt.category)
    nxt_prdt_no+=1
    save_products("product_data.json",products,nxt_prdt_no)
    return{"message":"Account create successfully","Product no": {nxt_prdt_no-1}}
@productapp.post("/restock/{prdt_no}")
def restock(prdt_no:int,qnt:int):
    if len(products)<=0:
        return{"error":"Create products first"}
    else:
        if qnt<=0:
            return{"message":"Stock count should be positive!"}
        else:
            products[prdt_no].restock(qnt)
            return{"Stocks is updated new stock count" : products[prdt_no].stock}
@productapp.post("/sellproduct/{prdt_no}")
def sell(prdt_no:int,qnt:int):
    if len(products)<=0:
        return{"error":"Create products first"}
    else:
        if qnt<0:
            return{"message":"Sell count should be positive!"}
        else:
            products[prdt_no].sell(qnt)
            return{"message":"Stock successfully sold","Stocks is updated new stock count" : products[prdt_no].stock}
@productapp.get("/islowstock")
def islowstock():
    if len(products)<=0:
        return{"error":"Create products first"}
    else:
        return{"Low stock products":{p_no:dtls.name for p_no,dtls in products.items() if dtls.islowstock()}}
