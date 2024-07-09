def calculater():   
    print('Welcome to calculater')
    print('select operation')
    print('1. Addition')
    print('2.Subtraction')
    print('3.Multiplication')
    print('4.Division')
# 
# 
    choice=input('enter the your choice: ')
    if choice in ('1','2','3','4'):
        num1=float(input("enter the 1'st number "))
        num2=float(input("enter the 2'st number "))
        if choice == '1':
            result=num1+num2
            print(f' your sum is: {num1}+{num2}={result}')
# 
        if choice == '2':
            result=num1-num2
            print(f'your subtraction is: {num1}-{num2}={result}')
# 
        if choice == '3':
            result=num1*num2
            print(f'your Multiplication is: {num1}*{num2}={result}')
# 
        if choice == '4':
            if (num2!=0):
                result=num1/num2
                print(f'your division is: {num1}/{num2}={result}')
            else:
                print('Error,Division by zero not valied.....')    
    else:
        print('invalid choise')  
        # 
calculater()