adventure = input("Which type of adventure should I have? ")  #Adventure variable will store user choice

if (adventure.lower() == "scary") or (adventure.lower() == "short"):  #If the answer is scary or short , this condition is True
    print("Entering the dark forest!")
elif (adventure.lower() == "safe") or (adventure.lower() == "long"):  #If the answer is safe or long, this condition is True
    print("Taking the safe route!")
else:
    print("Not sure which route to take.")      #If none of the previous conditions are being met, this message will be shown