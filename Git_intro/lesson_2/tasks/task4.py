num_1 = int(input("Введите число "))
num_2 = int(input("Введите второе число "))
math = input("Введите математическую операцию ")
if math == "+":
 print( num_1 + num_2)
elif math == "-":
  print(num_1 - num_2)
elif math == "*":
  print(num_1 * num_2)
elif math == "/":
   if num_2 != 0:
    print(num_1 / num_2)
   else:
    print(input("На ноль делить нельзя "))



