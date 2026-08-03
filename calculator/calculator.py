def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

while True:
    try:
        response = input("Choose an operation (+, -, *, /) or type 'quit' to exit: ").lower()
        if response == "quit" or response == "q":
            print("Goodbye!")
            break
        elif response in ["+", "-", "*", "/"]:
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))

            if response == "+":
                result = add(num1, num2)
            elif response == "-":
                result = subtract(num1, num2)
            elif response == "*":
                result = multiply(num1, num2)
            elif response == "/":
                result = divide(num1, num2)

            print(f"Result: {result}")
        else:
            print("Invalid option. Please choose +, -, *, /, or type 'quit'.")
    except ZeroDivisionError:
        print("Error: cannot divide by zero.")
    except ValueError:
        print("Error: please enter valid numbers.")