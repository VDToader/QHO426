cmd = input("Where should I move the paint brush ? (up, down, left, right)\n") # Will store user choice in one variable that will be compared afterwards

if cmd.lower() == "up":             # Added the .lower method just in case the user writes in upper case characters
    print("I am painting in the upward direction!")
elif cmd.lower() == "down":
    print("I am painting in the downward direction!")
elif cmd.lower() == "left":
    print("I am painting in the left direction!")
elif cmd.lower() == "right":
    print("I am painting in the right direction!")
else:
    print("You can select only one of the four movement indicated previously!") # If user's choice is not included in the four possibilities this message will be displayed