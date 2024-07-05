while True:
    try:
        a = int(input("Enter a first number:")) 
        b = int(input("Enter a second number:"))
        if a == 5:
            raise Exception('Input cannot be 5')
        print(a/b)
        
    except ZeroDivisionError:
        print('A number cannot be divisible by 0.')

    except ValueError:
        print('Input fields require only integer.')
    
    except Exception as e:
        print(f'Something went wrong!! error: {e}')
        
# student = [
#     'dipen', 'bimal', 'sher', 'virat', 'messi', 'dhoni', 'de villiers'
# ]

# total = len(student) - 1

# while True:
#     try:
#         index = int(input(f'Enter the number between 0 to {total}: '))
#         print(student[index])
#         break
    
#     except IndexError:
#         print(f"Cannot be greater than {total}")
#         break
        
#     except Exception as e:
#         print('There is something error.', e)
#         break
