from farm_example.animals.animal import Animal

class Cat(Animal):
    def __init__(self, name: str, preferred_food: set, age: int):
        super().__init__(name, preferred_food, age)
        self.say_word = "Мяу-Мяу"
        self.animal_type = "Кот"


    def treat(self, hours: int = 1) -> str:
        print(f'Мы играем с {self.name} {hours} часов')
        return 'очень хорошее настроение'