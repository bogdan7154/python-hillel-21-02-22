# гинератор который разделяет строку
def word_gen(s):
    words = s.split()
    for word in words:
        yield word


s = input('Введите строку: ')
for word in word_gen(s):
    print(word)
