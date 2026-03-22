print("=== SIMPLE CALCULATOR ===")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

option = int(input("Choose an operation (1-4): "))

if option in [1, 2, 3, 4]:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if option == 1:
        result = num1 + num2
        operation = "Addition"
        print(f"\n=== RESULT ===")
        print(f"Operation : {operation}")
        print(f"Result    : {result}")
    elif option == 2:
        result = num1 - num2
        operation = "Subtraction"
        print(f"\n=== RESULT ===")
        print(f"Operation : {operation}")
        print(f"Result    : {result}")
    elif option == 3:
        result = num1 * num2
        operation = "Multiplication"
        print(f"\n=== RESULT ===")
        print(f"Operation : {operation}")
        print(f"Result    : {result}")
    elif option == 4:
        if num2 == 0:
            print("Error: Cannot divide by zero")
        else:
            result = num1 / num2
            operation = "Division"
            print(f"\n=== RESULT ===")
            print(f"Operation : {operation}")
            print(f"Result    : {result}")
else:
    print("Invalid operation entered")