class Dog:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def eat(self):
        if self.gender == "boy":
            print(f"{self.name}, good boy, eatUp")
        else:
            print(f"{self.name}, good girl, eatUp")

    def bark(self, loud):
        if loud:
            print("WOOF WOOF WOOF")
        else:
            print("WOOF")


class Beagle(Dog):
    def __init__(self, name, gender, age, gunshy):
        super().__init__(name, gender, age)
        self.gunshy = gunshy

    def hunt(self):
        if self.gunshy:
            print(f"{self.name} is not good in hunting")
        else:
            print(f"{self.name} is so good in hunting")


beagle1 = Beagle("beagle1", "boy", 11, False)
beagle1.eat()
beagle1.hunt()
beagle2 = Beagle("beagle2", "girl", 12, True)
beagle2.eat()
beagle2.hunt()
