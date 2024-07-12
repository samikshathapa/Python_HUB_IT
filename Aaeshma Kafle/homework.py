
def average():
    a=int(input('enter number of grades to calculate:'))
    if a<0:
        print('number of grade should be positive')
        

    grades=[]
    for i in range(a):
        grade=float(input(f'enter grade {i+1}'))
        grades.append(grade)

    average_grade=sum(grades)/len(grades)
    print(f'average grade:{average_grade:.2f}')
    average()
