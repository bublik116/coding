def process(number):
    number1 = int(number)
    num = 0
    string1 = "proverka"
    if string1 =="":
        raise ValueError("Пустая строка")
    
    for num in range(number1):
        num1 = (num*num)
        num + 1
        print(num1)
        if num < number1:
            if num == 4:
                continue
            if num1 > 50:
                print(f"Квадрат числа {num} больше 50")
            if num1 < 20:
                print(f"Квадрат числа {num} меньше 20")
            if num1 >= 20 and  num1 <= 50:
                print(f"Квадрат числа {num}  больше  или равен  20 и меньше или равен  50")
            if num == 9:
                break
            
                
process(number = 10.0)

