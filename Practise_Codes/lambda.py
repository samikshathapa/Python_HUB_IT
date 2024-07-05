# lamba is anamous function means which doesnot have its name
# lambda returns function expression

# doubler(1): yo vaneko x ko value
# doubler  = func(1): yo vaneko n ko value

sum = lambda a,b:a+b

# print(sum(1,2))

def func(n):
    return lambda x:x*n

doubler = func(3)

print(doubler(10))