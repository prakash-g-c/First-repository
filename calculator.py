#My first project in python
#Define the function
def add(x, y) :
    return x + y

def sub(x, y) :
    return x - y

def mul(x, y) :
    return x * y

def divide(x, y) :
    return x // y

def power(x, y) :
    return pow(x, y)


#Take input value
print("Select the following operation\n" \
      "1.Add\n"\
      "2. Substract\n" \
      "3. Multiply\n" \
      "4. Divide\n" \
      "5. power\n"
      )
choice =int (input("Enter choice (1/2/3/4/5)"))
num1 =int(input("Enter the first number:"))
num2 =int(input ("Enter the second number:"))

if choice == 1:
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == 2:
    print(num1, "-", num2, "=", sub(num1, num2))
elif choice == 3:
    print(num1, "*", num2, "=", mul(num1, num2))
elif choice == 4:
    print(num1, "//", num2, "=", divide(num1, num2))
elif choice == 5:
    print(num1, "^", num2, "=", power(num1, num2))
else:
    print("Invalid input value")







