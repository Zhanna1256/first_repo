year = int(input("Введите год "))
if (year %4 ==0):
    print("Високосный")
elif (year %400 ==0):
    print("Високосный")
elif (year %100 ==0):
    print("Невисокосный")
else:
    print("Невисокосный")


