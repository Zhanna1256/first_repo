numb_1 = int(input("Введите число "))
if (numb_1 % 3 ==0) and (numb_1 % 5 ==0):
    print("FizzBuzz")
elif (numb_1 % 5 ==0):
    print("Buzz")
elif (numb_1 % 3 ==0):
    print("Fizz")
else:
    print(numb_1)


