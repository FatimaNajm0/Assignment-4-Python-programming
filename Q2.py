class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        print(f"Hello, my name is {self.name}!")

my_person = Person("Ali", 22)
my_person.greeting()
