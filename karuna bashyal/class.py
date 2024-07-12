

class person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def have_birthday(self):
        self.age += 1

    def display_info(self):
        print(f'name= {self.name}, age={self.age}')

person1 = person('karuna', 19)
print('before birthday:')
person1.display_info()

person1.have_birthday()
print('after birthday:')
person1.display_info()