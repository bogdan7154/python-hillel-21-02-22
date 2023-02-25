# узнаем данные от пользователя
gasoline_consumption = float(input("Введите расход на 100км: "))
gasoline_price = float(input("Введите цену 1л бензина: "))
distance = float(input("Введите растояние которое нужно проехать: "))

# вычисляем сколько уйдет бенза и стоимость
total_consumption = gasoline_consumption * distance / 100
result = total_consumption * gasoline_price

# даем понять что нужно покупать электрокар))
print("Витрати на паливо: {:.2f} грн".format(result))