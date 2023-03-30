# функция добавление записей
def add_note():
    note = input('Введіть нотатку: ')
    notes.append(note)


# функция перебирает элементы для сортивровки
def show_notes(sorted_notes):
    print('Нотатки:')
    for note in sorted_notes:
        print(note)


# Создаем пустой список
if __name__ == '__main__':
    notes = []

    # цикл диалога с пользователем
    while True:
        action = input('Введіть дію (add/earliest/latest/longest/shortest): ')

        if action == 'add':
            add_note()
        elif action == 'earliest':
            show_notes(sorted(notes))
        elif action == 'latest':
            show_notes(sorted(notes, reverse=True))
        elif action == 'longest':
            show_notes(sorted(notes, key=len, reverse=True))
        elif action == 'shortest':
            show_notes(sorted(notes, key=len))
        else:
            print('Невірна дія')

        if input('Продовжити? (y/n): ') != 'y':
            break
