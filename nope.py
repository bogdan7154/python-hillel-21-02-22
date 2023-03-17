user_palindrome = input('Введите строку которую хотите проверить на зеркальность: ')  # пользователь вводит строку
# переводим в нижний регистр, удаляем все пробелы , табуляции, символы пунктуации
ban_symbols = ['>', '.', ',', '-', ':', ';', '?', '!', '"', "'", "_", " "]
for i in range(len(ban_symbols)):
    user_palindrome = user_palindrome.lower().replace(ban_symbols[i], "")

# если строка user_palindrome равна своей зеркально строке то выполняется первый принт, иначе втрой
if user_palindrome == (user_palindrome[::-1]):
    print('строка является зеркальной')
else:
    print('строка не является зеркальной')
