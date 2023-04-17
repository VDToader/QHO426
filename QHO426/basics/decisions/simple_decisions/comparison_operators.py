first = int(input ("Please enter the first number.\n")) #added a new line command to match the same output as the exercise requested
second = int(input ("Please enter the second number.\n"))

if first < second:
    print ("First number is the smallest")
elif first > second:
    print ("Second number is the smallest")
else:
    print("Both numbers are equal") #The only possibility left is that both numbers are equal