activity = input("Enter an activity: ") # this line will get the activity name from the user

if activity.lower() == "calculate": #I am using lower method in case the user will use upper case letters
    print("Performing calculations....")
else:
        print("Performing activity...") #if the condition is not acompllished the program will run the other posibility
print("Activity completed ! ")
