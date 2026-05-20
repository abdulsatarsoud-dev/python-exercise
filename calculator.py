def calculator():
    print("~~~ Simple Calculator with Two input ~~~") # Show title of my program
    try:
        num1 = float(input("Enter First number: "))
        operation = input("Choose operation (+, -, *, /): ") 
        num2 = float(input("Enter Second number: "))

        if operation == "+":
            print(f"Result: {num1 + num2}")
        elif operation == "-":
            print(f"Result: {num1 - num2}")
        elif operation == "*":
            print(f"Result: {num1 * num2}")
        elif operation == "/":
            print(f"Result: {num1 / num2}" if num2 != 0 else "Math error, not divided by 0") # Show alert message for denominator to be zeo in division
        else:
            print("Invalid choice")
    except ValueError:
        print("Enter a number only")
if __name__ == "__main__":
    calculator()
 
 
    