# импортируем библиотеку
import math

# создаем в функции цыкл ввода с обработкой не правильного значения
def reading_values(comment):
    while True:
        num = float(input(comment))
        if num <= 0:
            print('Введите положительное  число')
        else:
            return num

# создаем функцию где проверяем треугольник на правильность
def triangle_existence_test(a, b, c):
    return (a + b > c) and (a + c > b) and (b + c > a)

# функция где вычисляем периметр
def calculate_perimetr(a, b, c):
    return a + b + c

# функция где вычисляем площадь
def calculate_area(a, b, c):
    p = calculate_perimetr(a, b, c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))

# диалог с пользователем. Узнаем значение сторон
if __name__ == '__main__':
    a = reading_values('Введите первую сторону треугольника: ')
    b = reading_values('Введите вторую сторону треугольника: ')
    c = reading_values('Введите третью сторону треугольника: ')

# сохраняем в переменную результаты цыклов  и выводим результат
    if calculate_perimetr(a, b, c):
        perimetr = calculate_perimetr(a, b, c)
        area = calculate_area(a, b, c)
        print(f'треугольник со сторонами {a},{b},{c} существует. Его периметр равен {perimetr:.2f}, а площадь {area:.2f}')
    else:
        print(f'треугольника со сторонами {a},{b},{c} не существует ')
