products = [("Хлеб", 40,20), ("Молоко", 60,15), ("Яблоки", 100,80)]
for product in products:
    print(f"Товар:{product[0]}, Цена:{product[1]}")


   
def min_price():
     for product in products:
        if product[1] < 80:
            print(f"Товар:{product[0]}")   
    
min_price()


