"""
Day7 10.17
练习
"""
# 定义父类：Animal
class Animal:
    def __init__(self, name, age, type):
        self.name = name
        self.age = age
        self.type = type

    def info(self):
        print(f"名字：{self.name}")
        print(f"年龄：{self.age}")
        print(f"种类：{self.type}")

    def make_sound(self):
        print("动物发出叫声")

# 定义子类:Cat
class Cat(Animal):
    def __init__(selfself, name, age, type="猫科"):
        super().__init__(name, age, type)

    def make_sound(self):
        print("喵喵喵~")

# 定义子类：Dog
class Dog(Animal):
    def __init__(self, name, age, type="犬科"):
        super().__init__(name, age, type)

    def make_sound(self):
        print("汪汪汪~")

# 定义子类：Duck
class Duck(Animal):
    def __init__(self, name, age, type="鸭科"):
        super().__init__(name, age, type)

    def make_sound(self):
        print("嘎嘎嘎~")

def animal_sound(animal):
    animal.make_sound()

if __name__ == '__main__':
    animal = Duck("小八", 14)
    animal.info()
    animal_sound(animal)