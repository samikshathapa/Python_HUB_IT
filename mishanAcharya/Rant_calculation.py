rent=int(input('enter your flat rent: '))
food=int(input('enter the amount of food ordered: '))
electricity_spend=int(input('enter the total electricity unit: '))
charge_per_unit=int(input('enter the charge per unit'))
person=int(input('enter the number of person living in room: '))

total_electristic= electricity_spend * charge_per_unit

total_rant= (rent+food+total_electristic)/person 

print(f'Total cost of 1 month per person:{total_rant} ')

