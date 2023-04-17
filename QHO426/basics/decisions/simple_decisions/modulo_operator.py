number = int(input ("Please enter a number: ")) # formatted the user input as a integer to avoid string type

if number % 2 == 0: #condition to check if the number is even
    print(f"The number {number} is an even number.")
elif number % 2 == 1: #condition to check if the number is odd
    print(f"The number {number} is an odd number.")
else:
    print(f"{number} is not a whole number. Try again !")