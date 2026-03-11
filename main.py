from product import Product
from storage import load_products,save_products
products,nxt_prdt_no=load_products("product_data.json")
prdt_no=None
while True:
    try:
        menu=int(input("\n1 for adding products\n2 for view all products\n3 for update stock\n4 for sell product\n5 for search product\n6 for check low stock\n7 for delete product\n8 for save data\n9 for exit\n\nChoose the method : "))
    except ValueError:
        print("\nEnter in number!")
        continue
    if menu==1:
        try:
            name=input("Enter product name : ")
            price=float(input("Enter price : "))
            stock=int(input("Enter Stocks count : "))
            categories=["Electronics","Clothings","Foods","Stationaries","Others"]
            category=input(f"{categories}\nChoose category : ")
            while category not in categories:
                category=input(f"\nWrong input Enyer again\n{categories}\nChoose category : ")
            products[nxt_prdt_no]=Product(nxt_prdt_no,name,price,stock,category)
            nxt_prdt_no+=1
        except ValueError:
            print("\nEnter in number!")
            continue
    elif menu==2:
        if len(products)<=0:
            print("\nadd products first")
            continue
        for p_no,dtls in products.items():
            print(f"{p_no}:{dtls}")
    elif menu==3:
        try:
            if len(products)<=0:
                print("\nadd products first")
                continue
            prdt_no=int(input(f"\nEnter product id for stock update : "))
            if prdt_no not in products:
                print("\nproduct not found")
                continue
            else:
                qnt=int(input("\nEnter new stocks count : "))
                while qnt<=0:
                    qnt=int(input("\nStocks count should be positive\nEnter new stocks count : "))
                products[prdt_no].restock(qnt)
        except ValueError:
            print("\nEnter in number!")
            continue
    elif menu==4:
        try:
            if len(products)<=0:
                print("\nNo products were created So can't sell\nadd products first")
                continue
            prdt_no=int(input(f"\nEnter product id for sell product : "))
            if prdt_no not in products:
                print("\nproduct not found")
                continue
            else:
                qnt=int(input("\nEnter solded product's count : "))
                while qnt<=0:
                    qnt=int(input("\nStocks count should be positive\nEnter new solded products count : "))
                products[prdt_no].sell(qnt)
        except ValueError:
            print("\nEnter in number!")
            continue
    elif menu==5:
        try:
            if len(products)<=0:
                print("\nNo products were created to search\nadd products first")
                continue
            else:
                search=input(f"\nEnter product name for search : ")
                for p_no,dtls in products.items():
                    if search.lower() ==dtls.name.lower():
                        print(products[p_no])
                        break
                else:
                    print("\nProduct name not match to anyone.")
        except ValueError:
            print("\nEnter in number!")
            continue
    elif menu==6:
        if len(products)<=0:
            print("\nadd products first")
            continue
        found=False
        for p_no,dtls in products.items():
            if products[p_no].islowstock():
                print(f"\n {dtls.name} product id : {p_no} is low stocks")
                found=True
        if not found:
            print("\nNo low stocks founded.")
    elif menu==7:
        try:
            if len(products)<=0:
                print("\nadd products first")
                continue
            prdt_no=int(input(f"\nEnter product no for delete : "))
            if prdt_no not in products:
                print("\nproduct not found")
                continue
            else:
                delete=int(input("\nDelete confirmation\n1 for yes\n2 for no\nchoose your option : "))
                if delete==1:
                    del products[prdt_no]
                    print(f"\nProduct {prdt_no} is deleted successfully")
                elif delete==2:
                    print("Option no is going to home menu.")
                    continue
                else:
                    print("\nInvalid input.")
        except ValueError:
            print("\nEnter in number!")
            continue
    elif menu==8:
        if len(products)<=0:
            print("\nadd products first")
            continue
        save_products("product_data.json",products,nxt_prdt_no)
        print("\nproduct saved successfully")
    elif menu==9:
        try:
            choice=int(input("\nDo you want to save or not\n\n1 for save\n2 for close without save\n\nchoose your option : "))
            if choice==1:
                save_products("product_data.json",products,nxt_prdt_no)
                print("\nproduct saved successfully.")
                break
            elif choice==2:
                print("Closing without save.")
                break
            else:
                print("\nInvalid input.")
        except ValueError:
            print("\nEnter in number!")
    else:
        print("\nInvalid input.")
