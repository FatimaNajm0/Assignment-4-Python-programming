class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary
        
    def display_salary(self):
        print(f"Salary: ${self.salary}")

my_employee = Employee("Ahmed", 1500)
my_employee.display_salary()
