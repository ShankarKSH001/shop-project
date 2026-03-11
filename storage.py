import json
from product import Product
def load_products(filename:str)->tuple:
    products={}
    try:
        with open(filename,"r") as file:
            data=json.load(file)
        nxt_prdt_no=data["nxt_prdt_no"]
        for prdt_no,details in data["products"].items():
            products[int(prdt_no)]=Product(int(details["prdt_no"]),str(details["name"]),float(details["price"]),int(details["stock"]),str(details["category"]))
    except(FileNotFoundError,json.JSONDecodeError,KeyError):
        nxt_prdt_no=101
    return products,nxt_prdt_no
def save_products(filename:str,products:dict,nxt_prdt_no:int)->None:
    data={
        "nxt_prdt_no":nxt_prdt_no,
        "products":{}
        }
    for prdt_no,details in products.items():
        data["products"][prdt_no]=details.to_dict()
    with open(filename,"w") as file:
        json.dump(data,file)
    print("\nData saved successfully")
