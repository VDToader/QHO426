ph = input("What phrase do you see? : ")
print("Reversing...")
i = 1
for i in range (1,(len(ph)+1)):     #Added +1 at the last parameter of the range because that value wasn't included in the range
    print(ph[-i],end="")            #This loop will print the last element of the string , and after each iteration the string index will decrease with 1
    i += 1