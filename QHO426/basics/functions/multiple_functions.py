def display_ladder(steps):          #First function will print the number of steps requested by the user
    count = 1
    while count <= steps:            #The while loop will repeat itself until the value of count variable will be
        print("| |\n***")            #less than equal with the number of steps.
        count += 1
def create_ladder():
    steps = int(input("How many steps remain? : ")) #The second function will store the user input inside a variable
    display_ladder(steps)                           #which is the parameter requested by the first function

create_ladder()
