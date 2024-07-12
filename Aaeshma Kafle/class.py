
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age 

    def  have_birthday(self):
            self.age+= 1

    def display_info(self):
        print(f"Name={self.name},Age={self.age}")

person1=person("Aaieshma",16)
print("Before Birthday:")
person1.display_info()

person1.have_birthday()
print("After Birthday:")
person1.display_info()