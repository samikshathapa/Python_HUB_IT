class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birthday(self):
        self.age += 1

    def display(self):
        print(f"Name = {self.name}, Age = {self.age}")

your_name = input("Enter the  name: ")
your_age = int(input("Enter the  age: "))
person1 = Person(name=your_name, age=your_age)

print("Before Birthday:")
person1.display()

person1.birthday()
print("After Birthday:")
person1.display()