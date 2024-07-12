def tryExcpt():
    file_name=input('Please Enter the name of the file to read: ')

    try:
        with open(file_name, 'r') as file:
               for x in file:
                    print(f'content of {file_name}  is :', x )
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
    except IOError as e:
        print(f"Error: An IOError occurred in '{file_name}'.")

tryExcpt() 