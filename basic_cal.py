"""Basic Calculator
Performs simple arithmetic operations."""
def calculator():
    print("Simple Calculator")
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            operation = input("Choose operation (+, -, *, /): ")

            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                if num2 == 0:
                    print("Cannot divide by zero.")
                    continue
                result = num1 / num2
            else:
                print("Invalid operation.")
                continue

            print(f"Result: {result}")
            cont = input("Perform another calculation? (y/n): ")
            if cont.lower() != 'y':
                break
        except ValueError:
            print("Invalid input. Please enter numeric values.")

if __name__ == '__main__':
    calculator()
