# узнаем показания и сумму тарифа
previous = float(input("Преждние показания электрического счетчика:"))
present = float(input("Теперешние показания:"))
rate = float(input("Сумма тарифа:"))

# вычисляем
result = (present - previous) * rate

# выводим резульат
print("За электроэнергию вам необходимо заплатить: {:.2f}".format(result))