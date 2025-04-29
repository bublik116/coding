def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
my_file = open("factor", "w+")
my_file.write(str(factorial(11)))
my_file.close()
my_file = open("factor", "r")
print(my_file.read())
