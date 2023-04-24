print("Create your character! \nWhich type of combat do you prefer ? \n1.Melee \n2.Ranged \n3.Magic")
cls  = input("I want to be ")           #This is a RPG character creation menu where users can choose the type of attack and one of their specific classes.

if (cls.lower() == "melee") or (cls == "1"):    #If the user response stored in cls variable is melee or 1, user need to selec a class as Warrior/Berserker/Paladin
    print(f"You choice is: {cls.upper()}")
    spec = input("Which is the right class for you? \n1.Warrior \n2.Berserker \n3.Paladin\nI want to be:")
    if (spec.lower() == "warrior") or (spec == "1"):    #Nested condition for the Melee class
        print(f"You are a Melee Warrior")
    elif (spec.lower() == "berserker") or (spec == "2"):
        print(f"You are a Melee Berserker")
    elif (spec.lower() == "paladin") or (spec == "3"):
        print(f"You are a Melee Berserker")
    else:                                               #If the answer is not one of the 3 classes
        print("You can be only a Melee: Warrior/Berserker/Paladin!")

elif (cls.lower() == "ranged") or (cls == "2"):
    print(f"You choice is: {cls.upper()}")
    spec = input("Which is the right class for you? \n1.Archer \n2.Hunter \n3.Marksmen\nI want to be:")
    if (spec.lower() == "archer") or (spec == "1"):
        print(f"You are a Ranged Archer")
    elif (spec.lower() == "hunter") or (spec == "2"):
        print(f"You are a Ranged Hunter")
    elif (spec.lower() == "marksmen") or (spec == "3"):
        print(f"You are a Ranged Marksmen")
    else:
        print("You can be only a Ranged: Archer/Hunter/Marksmen!")

elif (cls.lower() == "magic") or (cls == "3"):
    print(f"You choice is: {cls.upper()}")
    spec = input("Which is the right class for you? \n1.Sorcerer \n2.Priest \n3.Warlock\nI want to be:")
    if (spec.lower() == "sorcerer") or (spec == "1"):
        print(f"You are a Magic Sorcerer")
    elif (spec.lower() == "priest") or (spec == "2"):
        print(f"You are a Magic Priest")
    elif (spec.lower() == "warlock") or (spec == "3"):
        print(f"You are a Magic Warlock")
    else:
        print("You can be only a Magic: Sorcerer/Priest/Warlock!")

else:                                               #If the cls variable is not 1/2/3 or Melee/Ranged/Magic, this message will pop out
    print("You can be only Melee/Ranged/Magic")

