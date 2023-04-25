rows = int(input("How many rows should I have? : "))
columns = int(input("How many columns should I have? : "))

for r in range(rows):
    print(" ")       #   for each row we will print an empty space
    for c in range(columns):
        print(":-)",end="")