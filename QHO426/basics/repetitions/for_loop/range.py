br = int(input("What level of brightness is required? "))
if br % 2 == 0:                                #Will check if the input is an even number
    print("\nAdjusting brightness....")
    i = 0
    for i in range (0,br,2):                    #For every even number in the range 0 - user input, both of print statements will be shown
        print("\nBeep's brightness level: " + (i+2)*"*")
        print("Bop's brightness level: " + (i+2) * "*")
        i+=2
else:
    print("Please insert an even number")       #Added a condition in case the user response is not an even number