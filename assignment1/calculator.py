def calculator(choice, a, b):
    if choice == 1:
        return a + b
    elif choice == 2:
        return a - b
    elif choice == 3:
        return a * b
    elif choice == 4: 
        if b != 0:
            return a / b
        else:
            return "Error! Division by zero."
    else:
        return "Invalid choice!"

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = int(input("Enter choice (1/2/3/4): "))
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

result = calculator(choice, num1, num2)
print("Result:", result)
