print("--- Simple Calculator ---\n")
running = True
while running:
    print("Availible operations:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Devide")
    print("5. Exit\n")
    operation = int(input("Enter your choice:"))
    match operation:
        case 1:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            result = num1 + num2
            print("Result:", result)
        case 2:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            result = num1 - num2
            print("Result:", result)
        case 3:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            result = num1 * num2
            print("Result:", result)
        case 4:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            result = num1 / num2
            print("Result:", result)
        case 5:
            running = False
print("Exiting program...")
