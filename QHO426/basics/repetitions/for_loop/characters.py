char = input("What strange characters do you see? : ")
i = 0
for i in range (0, len(char)):
    print(f"Index {i} : {char[i]}")
    i += 1
print("Done!")