print("Program Started!")
char = input ("Please enter a standard character: ")

#If statement to check if the user inserted only one character
if len(char) == 1:
    print(f"The ASCII code for {char} is {ord(char)}")
print("Program Ended!")