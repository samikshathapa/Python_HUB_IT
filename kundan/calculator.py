def add(n1,n2):
    print(f'The sum of {n1} and {n2} is {n1+n2}')
def sub(n1,n2):
    print(f'The subtraction of {n1} and {n2} is {n1-n2}')
def mul(n1,n2):
    print(f'The multiplication of {n1} and {n2} is {n1*n2}')
def div(n1,n2):
    print(f'The division of {n1} and {n2} is {n1/n2}')

user = input('''Choose an operation!!!!
Enter + for addition.
Enter - for subtraction.
Enter * for multiplication.
Enter / for division. ''')

if user =='+':
    n1 = float(input('Enter first number='))
    n2 = float(input('Enter second number='))
    add(n1,n2)
elif user =='-':
    n1 = float(input('Enter first number='))
    n2 = float(input('Enter second number='))
    sub(n1,n2)
elif user =='*':
    n1 = float(input('Enter first number='))
    n2 = float(input('Enter second number='))
    mul(n1,n2)
elif user =='/':
    n1 = float(input('Enter first number='))
    n2 = float(input('Enter second number='))
    div(n1,n2)
else:
    print('Invalid Input')
