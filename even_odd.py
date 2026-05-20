def check_even_or_odd():
    print("--- Check if a number is even or odd--- ")

num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is an Even number")
else:
    print(f"{num} is an Odd number")

if __name__ == "__main__":
    check_even_or_odd()
