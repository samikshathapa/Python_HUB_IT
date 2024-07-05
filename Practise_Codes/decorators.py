
# def star(func):
#     def wrapper():
#         print("*"*10)
#         func()
#         print("*"*10)
    
#     return wrapper

# @star   
# def hello():
#     print("Hello function")

# @star   
# def bye():
#     print("bye")
    
# # star(hello)()
# hello()
# # bye()

# def star(func):
#     def wrapper():
#         print('*')
#         func()
#         print('*****')
        
#     return wrapper

# def hashtag(func):
#     def hash():
#         print('#')
#         func()
#         print('#######')
        
#     return hash

# @star
# @hashtag
# def hello():
#     print("This is for hello")
    
# hello()    
# # hashtag(hello)()

def make_pretty(func):
    def inner():
        print("I got decorated.")
        func()
    return inner

@make_pretty
def ordinary():
    print("I am ordinary.")
    
ordinary()
    
# make_pretty(ordinary)()

# above 'make_pretty(ordinary)()' this line and below line are same
# decorated_func = make_pretty(ordinary)
# decorated_func()

