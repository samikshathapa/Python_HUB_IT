# sets doesnot contain duplicate items

fruits = {
    'banana', 'apples', 'grapes', 'oranges', 'mangoes'
}

vegetables = {
    'cabbage', 'pumpkin', 'grapes', 'carrot', 'cauli flower'
}

a = {1,2,3,4,5}
b = {4,3,2,5,1}

# print(len(fruits))
# fruits.add('cherry')
# print(fruits)

# fruits.remove('grapes')
# print(fruits)

# fruits.update(vegetables)
# print(fruits)

# print('Union using union():', fruits.union(vegetables))
# print('Union using |:', fruits|vegetables)

# print('Intersection using &:', fruits & vegetables)
# print('Intersection using intersection():', fruits.intersection(vegetables))

# print('Difference using differnce:', fruits.difference(vegetables))
# print('Difference using - :', fruits-vegetables)

# print('Symmetric difference using ^:', fruits ^ vegetables)
# print('Symmetric_difference():', fruits.symmetric_difference(vegetables)) 

if a == b:
    print('Sets are same')
else:
    print('Sets are different')
    