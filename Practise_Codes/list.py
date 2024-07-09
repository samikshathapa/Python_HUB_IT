address = [
    "butwal","Haraiya","chitwan","pokhara","hetauda","kapilbastu"
]
# print(address[1:])
# print(address[0::2])
print(address[::-1])

#add 
address.append("Dang")
print(address)
address.insert(5,"palpa")
print(address)
#remove
address.remove("butwal")
print(address)

address.pop(4)
print(address)
#list concatanation
a = ["apple","banana","grape"]
b = ["mango","pineapple","peach"]
c = a+b
print(c)
#lengh of the  address
print(len(address))

p = [["apple","chhery"],["bus","car"]]
print(p)
print(p[1:])