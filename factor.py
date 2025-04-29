
try:
 with open("factor") as f:
 print(f.read())
except FileNotFoundError:
 print("Файл не найден")
