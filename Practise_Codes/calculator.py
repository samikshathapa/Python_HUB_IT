a = int(input("Enter first number:"));
b = int(input("Enter second number:"));

print("What do you want to perform?")

operator = input("Enter an operator [+, -, *, /]: ")

if operator == '+':
    sum = a + b;
    print(f"Sum of {a} and {b} is: {sum}.")

elif operator == '-':
    diff = a - b;
    print(f"Difference of {a} and {b} is: {diff}.")

elif operator == '*':
    mul = a * b;
    print(f"Multiply of {a} and {b} is: {mul}.")

elif operator == '/':
    if b==0:
        print("The denumerator is 0 so it cannot be divided.")
    else:
        div = a / b;
        print(f"Division of {a} and {b} is: {div}.")
    
else:
    print("Invalid operator")