def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


def calculator():
    print("===== PYTHON CALCULATOR =====")
    print("Choose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter choice (1/2/3/4): ").strip()

    if choice not in {'1', '2', '3', '4'}:
        print("Invalid choice.")
        return

    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    try:
        if choice == '1':
            result = add(a, b)
        elif choice == '2':
            result = subtract(a, b)
        elif choice == '3':
            result = multiply(a, b)
        else:
            result = divide(a, b)
    except Exception as e:
        print("Error:", e)
    else:
        print("Result:", result)


if __name__ == "__main__":
    calculator()
