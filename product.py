class Product:
    def __init__(self,prdt_no:int,name:str,price:float,stock:int,category:str):
        self.prdt_no=prdt_no
        self.name=name
        self.price=price
        self.stock=stock
        self.category=category
    @property
    def price(self)->float:
        return self._price
    @price.setter
    def price(self,value):
        if value<0:
            print("\nPrice must be positive,Price set to 0")
            self._price=0
        else:
            self._price=value
    @property
    def stock(self):
        return self._stock
    @stock.setter
    def stock(self,value):
        if value<0:
            print("\nStock should be positie,stock set to 0")
            self._stock=0
        else:
            self._stock=value
    @property
    def category(self):
        return self._category
    @category.setter
    def category(self,value):
        categories=["Electronics","Clothings","Foods","Stationaries","Others"]
        if value not in categories:
            print(f"Invalid categories\nChoose from {categories}")
            self._category="Others"
        else:
            self._category=value
    def __str__(self):
        return f"prdt_no:{self.prdt_no},name : {self.name}\nprice={self.price}\nstock={self.stock}\ncategory={self.category}"
    def to_dict(self)->dict:
        return{
            "prdt_no":self.prdt_no,
            "name":self.name,
            "price":self.price,
            "stock":self.stock,
            "category":self.category
            }
    def restock(self,qnt:int)->None:
        while qnt<0:
            qnt=int(input("\nStock count can't be negetive\nEnter new stock count : "))
        self._stock+=qnt
        print(f"New stock count set for product no:{self.prdt_no}")
    def sell(self,qnt:int)->None:
        while qnt<=0:
            qnt=int(input("Self count can't be negetive\nEnter new sell count : "))
        self._stock-=qnt
        print(f"Stock updated.\nNew stock count for product no : {self.prdt_no} is {self._stock}")
    def islowstock(self)->bool:
        if self._stock>10:
            return False
        else:
            return True
