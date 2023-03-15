numbers = []    # создаем пустой список и затем цыкл while
while True:
    user_input = input("Введіть число або 'sum' для підсумовування: ")  # запрашиваем значение
    if user_input == "sum":     # если в переменную пользователь введет sum то
        print(f"Сума введених чисел: {sum(numbers)}")   # выведится ссума чисел
        break
    try:    # обрабатываем случай если пользователь введет не число
        number = float(user_input)    # Если введенное значение можно преобразовать в число, то программа продолжает работу
        numbers.append(number)
    except ValueError:  # а вот если нет
        print("Некоректне введення. Введіть число або 'sum' для підсумовування.")
x = [1, 5, 8, 9, 10]
print(x[::-1])


text = input('Введите текст со скобками: ')
while '(' in text:
    beginning_of_text = text.find('(')
    end_of_text = text.find(')')
    text = text[:beginning_of_text] + text[end_of_text+1:]

print(text)