# print(list(range(2,10)))

# for i in range(10):
#     print(i)
    
fruits = {
    'apples', 'mangoes', 'grapes', 'pomegranate', 'litchi'
}

# enumerate le tuple ma change gardinxa
for index,fruit in enumerate(fruits):
    print(index,fruit)
    # we can use index+1, index+2 and so on
    
    if fruit == 'litchi':
        break 
        
# name = "Dipen"

# for char in name:
#     print(char)