# file = open('example.txt')
# file_read = file.read()
# print(file_read)
# # file.close()

# with open('example.txt','r') as file:
#     file_read = file.read(8)
#     print(file_read)
#     file.close()
with open('example.txt','r') as file:
    # for x in file:
    #     print(x)
        f = open('example.txt', 'a')
        f.write("i am learning python")
        f.close()
