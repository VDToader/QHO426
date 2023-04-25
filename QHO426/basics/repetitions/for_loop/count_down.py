distance = int(input("How far are we from the cave? : "))
i = 0
for i in range (0, distance):
    print(f"{distance - i} steps remaining")   #The number of steps will be the total distance - the current loop number (i)
    i += 1
print("We have reached the cave!")