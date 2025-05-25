time = int(input("Введите время "))
if (time > 6 or time == 6) and (time  < 11 or time == 11):
    print("Утро")
elif (time > 12 or time == 12) and (time <17 or time == 17):
    print("День")
elif (time > 18 or time == 18) and (time < 23 or time == 23):
    print("Вечер")
else:
    print("Ночь")