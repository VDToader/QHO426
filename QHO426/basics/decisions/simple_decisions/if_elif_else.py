cmd = input("Where should I move the paint brush ? (up, down, left, right)\n")

if cmd.lower() == "up":
    print("I am painting in the upward direction!")
elif cmd.lower() == "down":
    print("I am painting in the downward direction!")
elif cmd.lower() == "left":
    print("I am painting in the left direction!")
elif cmd.lower() == "right":
    print("I am painting in the right direction!")
else:
    print("You can select only one of the four movement indicated previously!")