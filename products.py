products = [("Хлеб", 40,20), ("Молоко", 60,15), ("Яблоки", 100,80)]
spisok = []
def min_price():
    total_price = 0
    total_value = 0
    
    for product in products:
        global spisok
        quantity = product[2]
        price = product[1]
        total_value = quantity * price
        spisok.append(total_value)
    print(spisok)
    
        
        
         
min_price()
