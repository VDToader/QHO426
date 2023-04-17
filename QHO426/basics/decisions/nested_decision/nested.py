cover = input("What type of cover does the book have?\n")
if cover.lower() == "soft":
    answer = input("Is the book perfect bound?\n")
    if answer.lower() == "yes": # first condition in the nested if statement
        print("Soft cover, perfect bound books are very popular")
    else:                       # second condition in the nested if statement
        print("Soft covers with coils or stitches are great for short books") #for any answer other than 'yes' this message will be shown

elif cover.lower() == "hard":  #this is the second condition from the primary if loop
    print("Books with hard covers can be more expensive!")