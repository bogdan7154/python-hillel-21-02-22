from random import randint, choices


class Cat:
    def __init__(self, name: str, gender: str, age: int,
                 breed: str, play_hours: int, preferred_food: set
                 ):
        self.name = name
        self.gender = gender
        self.age = age
        self.breed = breed
        self.play_hours = play_hours
        self.preferred_food = preferred_food
        self.hungry = False
        self.cat_play = False

    def __str__(self) -> str:
        return f'{self.name.title()}, {self.age} лет породы {self.breed}'

    def mew(self):
        print(f'{self.name} мяукает!')

    def play(self):
        if self.play_hours == 0:
            print(f'{self.name} не гуляет')
            no_play_cat.append(cat)
        else:
            print(f'{self.name} гуляет {self.play_hours} часов')
            print('Ждем...')
            self.cat_play = True
            self.mew()
            print('Мяукает потому что доволен!!!')
        print(f'{self.name} проголодался')
        self.hungry = True

    def eat(self, suggested_food: str):
        if suggested_food in self.preferred_food:
            print(f'{self.name} кушает {suggested_food}')
            print(f'{self.name} мурчит потому что сытый')
            print(f'{self.name} пошел спать потому что наелся')
            self.hungry = False
        else:
            print(f'{self.name} предложили {suggested_food}, но мы такого не едим')


if __name__ == '__main__':
    fima = Cat('Фима', 'М', 9, 'британец', randint(0, 5), {'корм', 'рыбная овсянка'})
    felix = Cat('Феликс', 'М', 14, 'перс', randint(0, 5), {'корм', 'сметана'})
    vasya = Cat('Вася', 'М', 7, 'Неизвестно', randint(0, 5), {'мышь', 'молоко', 'рыба', 'сметана'})
    valera = Cat('Валера', 'M', 3, 'Сфинкс', randint(0, 5), {'корм'})
    garfield = Cat('Гарфилд', 'М', 5, 'Американский короткошерстный', randint(0, 5), {'лазанья', 'рыба', 'мясо'})
    whiskers = Cat('Вискас', 'Ж', 2, 'Шотландская вислоухая', randint(0, 5), {'корм', 'сметана', 'рыба'})

    potential_food = ['корм', 'рыбная овсянка', 'сметана', 'мышь', 'молоко', 'рыба']
    hungry_cat = list()
    no_play_cat = list()
    for cat in [fima, felix, vasya, valera]:
        print('=' * 20, f'\n Обычный день {cat}:')
        cat.mew()
        cat.play()
        for food in choices(potential_food, k=2):
            cat.eat(food)
        if cat.hungry:
            hungry_cat.append(cat)
            print('не спал всю ночь потому что был голодный и мешал спать хозяину')

    if hungry_cat:
        print(f'Найден(ны) {len(hungry_cat)} голодный(ых) кот(ов), срочно покормите!')
        print(' вот их имена:', ', '.join([cat.name for cat in hungry_cat]))

    if no_play_cat:
        print(f'Найден(ны) {len(no_play_cat)} не гулявших кот(ов), срочно вывустите кота во двор!')
        print(f'Вот их имена:', ', '.join([cat.name for cat in no_play_cat]))
