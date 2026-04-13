class Animal:
    def __init__(self, age, color):
        self.age = age
        self.color = color

    def animalVoice(self):
        print("This animal makes a sound.")

class Dog(Animal):
    def animalVoice(self):
        print("Woof!")

class Sheep(Animal):
    def animalVoice(self):
        print("Baa!")

my_dog = Dog(3, "Black")
my_sheep = Sheep(2, "White")

print(f"Dog - Age: {my_dog.age}, Color: {my_dog.color}")
print(f"Sheep - Age: {my_sheep.age}, Color: {my_sheep.color}")
