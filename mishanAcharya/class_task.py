# class define
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    # method define
    def birthday(self):
        self.age+=1
        print(f"Name = {self.name}, Age = {self.age}")
        
    def display(self):    
        print(f"Name = {self.name}, Age = {self.age}")
        
user_name=input("enter the name: ")
user_age=int(input("enter the age: "))
# cretae object
user=person(name=user_name ,age= user_age)

print("before Birthday: ")
#call object
user.display()


print("After Birthday: ")
user.birthday()
