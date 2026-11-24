class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    def bark(self):
        print("Bark")


class Cat(Mammal):
    def walk(self):
        print("Walk")


dog1 = Dog()
dog1.walk()
dog1.bark()
