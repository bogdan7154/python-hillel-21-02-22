# функция гениратор чисел фибоначчи
def fibonacci_gen(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b


n = int(input('введите конечный индекс элемента для генерации чисел Фибоначчи: '))


# Генерируем последовательность чисел Фибоначчи к n-му элементу
for num in fibonacci_gen(n):
    print(num)
