import os

# Функция добавления записи
def add_note():
    note = input('Введите заметку: ')
    notes.append(note)


# Функция отображения заметок
def show_notes(sorted_notes):
    print('Список заметок:')
    for note in sorted_notes:
        print(note)


# Функция сохранения заметок в файл
def save_notes_to_file(file_name):
    with open(file_name, 'w') as f:
        for note in notes:
            f.write(note + '\n')


# Функция загрузки заметок из файла
def load_notes_from_file(file_name):
    if os.path.isfile(file_name):
        with open(file_name, 'r') as f:
            for line in f:
                notes.append(line.strip())


# Определяем имя файла для хранения заметок
file_name = 'save.txt'

# Создаем пустой список заметок
notes = []

# Загружаем заметки из файла
load_notes_from_file(file_name)

# Цикл диалога с пользователем
while True:
    action = input('Введите действие (add/earliest/latest/longest/shortest/save & exit): ')

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
    elif action == 'save & exit':
        save_notes_to_file(file_name)
        break
    else:
        print('Некорректное действие')

    if input('Продолжить? (y/n): ') != 'y':
        break
