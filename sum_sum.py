# создаем  переменную с нулевым значением и запускаем цыкл
total = 0
while True:
    # запрашиваем у пользователя значение
    text = input('Введіть число або sum для підсумовування:')
    # если значение равно sum то программа выводит значение переменной и заканчивает цыкл
    if text == 'sum':
        print(total)
        break
        # тут мы применяем replace так как  если в строке есть точка, то isnumeric вернет False
    elif text.replace('.', '').isdigit() or (text.startswith('-') and text[1:].replace('.', '').isdigit()):
        # если значение число то оно плюсюется к переменной total
        total += float(text)
        # иначе программа выдаст пользователю о не коректном вводе
    else:
        print('Некоректне введення. Введіть число або sum для підсумовування')
