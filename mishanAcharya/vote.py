while True:
    try:
        age=int(input('enter the age of he/she: '))
        if age> 18:
            print('He/She can vote.........')
            break   
        else:
            print('He/She cannot vote.......')
        break      
    except ValueError:
        print('Error: please enter valid age. Please try again')
    