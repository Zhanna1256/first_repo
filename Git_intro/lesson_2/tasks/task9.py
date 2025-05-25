print ("Выберите фигуру: \n 1.Треугольник \n 2.Круг \n 3.Прямоугольник")
figure = input ("Выберите фигуру ")
if (figure == "1"):
    base = float(input("Введите основание треугольника: "))
    height = float(input("Введите высоту треугольника: "))
    s = 0.5 * base * height
    print(f"Площадь треугольника: {s}")
elif (figure == "2"):
    radius = float(input("Введите радиус круга: "))
    s = 3.14 * radius**2
    print(f"Площадь круга: {s}")
elif (figure == "3"):
    length = float(input("Введите длину прямоугольника: "))
    width = float(input("Введите ширину прямоугольника: "))
    s = length * width
    print(f"Площадь прямоугольника: {s}")
else:
    print("Неверный выбор")
    