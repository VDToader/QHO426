import random as rnd


min = int(input("Enter the minimum value: "))
max = int(input("Enter the maximum value: "))
x = rnd.randrange(min,max)
choice = int(input(f"I am thinking of a number between {min} and {max}. Can you guess what it is? "))

if choice < x :
    print("Your guess is too low")
elif choice > x :
    print("Your guess is too high")
elif choice == x:
    print("Congratulation! You've guessed the correct number!")
else:
    print("Try again")



