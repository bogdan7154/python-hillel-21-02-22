while True:
    text = input('Введіть повідомлення: ').lower()

    if 'привіт' in text or 'хай' in text or 'доброго дня' in text:
        print('Доброго вечора, я бот з України')
    elif 'як справи?' in text or 'що робиш?' in text or 'чим займаєшся?' in text:
        print('Вчусь програмувати на Python!')
    elif 'фільм' in text or 'кінотеатр' in text or 'серіал' in text:
        print('Соррі, що втручаюсь, не знаю про що йдеться мова, але подивіться серіал "Паперовий будинок", він просто бомба!')
    elif 'бувай' in text or 'надобраніч' in text or 'до зустрічі' in text:
        print('Побачимось у мережі, бувай!')
        break
    else:
        print('Дуже цікаво, але, на жаль, нічого не зрозуміло :(')
