sound = input("What did I hear? ")      #sound variable will store the first answer
object = input("What did I see? ")      #object variable will store the second answer

if (sound.lower() == "grr") and (object.lower() == "two red eyes"): #If the first answer is grr and the second one is two red eyes
    print("There is a scary creature. I should get out of here!")   #This message will be printed for the user
else:
    print("I am a little bit scared but I will continue.")          #If both or one of the previous conditions are not fulfilled this msg will be displayed