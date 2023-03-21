# функция для ввода сторон треугольника пользователем с обработкой ошибок ввода
def reading_values(comment):
    while True:
        num = input(comment)
        if num.isdigit() and float(num) > 0:
            return float(num)
        else:
            print('Введите положительное число')


# создаем функцию где проверяем треугольник на правильность
def triangle_existence_test(a, b, c):
    return (a + b > c) and (a + c > b) and (b + c > a)


# функция где вычисляем периметр
def calculate_perimeter(a, b, c):
    return a + b + c


# функция для вычисления площади треугольника
def calculate_area(a, b, c):
    p = calculate_perimeter(a, b, c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5


# функция для определения типа треугольника
def get_triangle_type(a, b, c):
    if a == b == c:
        return 'равносторонний'
    elif a == b or b == c or a == c:
        if a ** 2 + b ** 2 == c ** 2 or b ** 2 + c ** 2 == a ** 2 or a ** 2 + c ** 2 == b ** 2:
            return 'прямоугольный'
        else:
            return 'равнобедренный'
    elif a ** 2 + b ** 2 == c ** 2 or b ** 2 + c ** 2 == a ** 2 or a ** 2 + c ** 2 == b ** 2:
        return 'прямоугольный'
    else:
        return 'обычный'


# диалог с пользователем. Узнаем значение сторон
if __name__ == '__main__':
    a = reading_values('Введите первую сторону треугольника: ')
    b = reading_values('Введите вторую сторону треугольника: ')
    c = reading_values('Введите третью сторону треугольника: ')

    # проверяем наличие треугольника и выводим результат
    if triangle_existence_test(a, b, c):
        perimeter = calculate_perimeter(a, b, c)
        area = calculate_area(a, b, c)
        triangle_type = get_triangle_type(a, b, c)
        print(f'Треугольник со сторонами {a}, {b}, {c} является {triangle_type}. Его периметр равен {perimeter:.2f}'
              f', а площадь {area:.2f}')
    else:
        print(f'Треугольника со сторонами {a}, {b}, {c} не существует')
