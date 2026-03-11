from product import Product
def test_restock():
    prdt=Product(101,"apple",50.00,20,"Foods")
    prdt.restock(50)
    assert prdt.stock==70
def test_sell():
    prdt=Product(101,"apple",50.00,20,"Foods")
    prdt.sell(10)
    assert prdt.stock==10
def test_islowstock():
    prdt=Product(101,"apple",50.00,9,"Foods")
    assert prdt.islowstock()
def test_negative_price():
    prdt=Product(101,"apple",-50.00,9,"Foods")
    assert prdt.price==0
