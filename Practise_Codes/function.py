# name = 'virat'

# def greeting():
#     print(f"Hello its me {name}")
    
# greeting()

# def greeting(fname):
#     print(f"Hello its me {fname}")
    
# greeting(fname='virat')

# def sum(*numbers):
#     total = 0
#     for number in numbers:
#         total +=number
#     print(total)
    
# sum(1,2,3,4,5,6)

def person(**attr):
    for key,value in attr.items():
        print(f"{key} : {value}")
    
person(name='dipen',age=23)