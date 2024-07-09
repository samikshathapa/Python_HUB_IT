# !readlines() convert every line to list


# To write in a file
# file = open('file.txt', 'w')
# file.write('I am learning Python with Django course.')

# To read a file
# file = open('file.txt')
# read_content = file.readlines()
# print(read_content)
# file.close()

# Append Mode
# try:
#     f = open('file.txt', 'a')
#     f.write('\nMindrisers Company')
#     f.close()
# except FileNotFoundError:
#     print('File is not found! Plz make file first.')
    
# Write mode
# try:
#     f = open('file.txt', 'w')
#     f.write("Currently Iam learning Django.")
# except Exception as e:
#     print('Error:', e)

import os
from time import sleep 

try:
    f = open('file100.txt', 'a')
    f.write("Currently Iam learning Django.")
    f.close()
    # sleep(3)
    # os.remove('file.txt')
except Exception as e:
    print('Error:', e)
    
