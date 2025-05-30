time = int(input("Введите время "))
if (6<=time<=11):
    print("Утро")
elif (12<=time<=17):
    print("День")
elif (18 <=time<=23):
    print("Вечер")
elif (0<=time<=5):
    print("Ночь")
else:
    print("Ошибка")