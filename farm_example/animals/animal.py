class Animal:

    def __init__(self, name: str, preferred_food: set, age: int):
        """
        :param name: имя животного
        :param preferred_food: перечень употребляемой еды
        :param age: возраст животного
        """

        self.name = name
        self.preferred_food = preferred_food
        self.age = age

        self.say_word = "???"
        self.animal_type = "Животное"

        self.__hungry = True



    @property
    def hungry(self):
        return self.__hungry

    @hungry.setter
    def hungry(self, x):
        """
        Hungry может быть только булевым значением
        По логике работы программы можно только проголодаться
        Чтобы утолить голод, недостаточно присвоить False в hungry
        Нужно вызвать метод eat
        :param x:
        :return:
        """
        if isinstance(x, bool):
            if x:
                self.__hungry = True

    def __str__(self):
        return f"{self.animal_type} по имени {self.name}, {self.age} лет."

    def eat(self, food: str):
        """

        :param food:
        :return:
        """
        if food in self.preferred_food:
            print(f"{self.name} кушает {food}")
            self.__hungry = False
        else:
            print(f"{self.name} такое не ест: {food}")

    def say(self):
        """

        :return:
        """
        print(f"{self.name} говорит: {self.say_word}. Голод животного: {self.__hungry}")

    def treat(self, hours: int = 1):
        """
        Ухаживать ха животным, переопределяется наследниками
        :param hours:
        :return:
        """
        print(f"Вы ухаживаете за {self.name} {hours} час(ов)")
        if self.__hungry:
            print(f"{self.name} голодное!")


if __name__ == '__main__':
    a = Animal(None, {None}, None)
    print(hasattr(a, 'name'))
    print(hasattr(a, 'nameee'))
    print()
