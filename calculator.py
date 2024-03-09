def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        print("Error: Division by zero is not allowed.")
        return None
    else:
        return x / y

def display_history(history):
    if not history:
        print("No calculations yet.")
    else:
        print("Calculation History:")
        for i, (operation, num1, num2, result) in enumerate(history, start=1):
            print(f"{i}. {operation} {num1} and {num2} = {result}")

def main():
    history = []
    while True:
        print("\nCalculator Menu:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Show History")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")
        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            if choice == '1':
                result = add(num1, num2)
                operation = "Addition"
            elif choice == '2':
                result = subtract(num1, num2)
                operation = "Subtraction"
            elif choice == '3':
                result = multiply(num1, num2)
                operation = "Multiplication"
            else:
                result = divide(num1, num2)
                operation = "Division"
            if result is not None:
                print(f"Result: {result}")
                history.append((operation, num1, num2, result))
        elif choice == '5':
            display_history(history)
        elif choice == '6':
            print("Exiting calculator...")
            break
        else:
            print("Invalid choice. Please enter a valid choice (1-6).")

if __name__ == "__main__":
    main()