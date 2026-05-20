def multiplication_table():
    try:
        num =int(input("Enter a number: "))
        print(f"\n--- Multiplication table of {num} ---")
        for i in range(1, 11) :
            print(f"{num} x {i} = {num * i}") # Show the multiplied number in table
    except ValueError:
        print("Choose the natural number")

if __name__ == "__main__":
    multiplication_table()
