question_1 = input("Where should I look? \n")
if question_1 == "in the bedroom":                              #First Decision
    answer_1 = input("Where in the bedroom should I look? \n")  #If the answer1 is 'under the bed' the first nested decision will start
    if answer_1 == "under the bed":                             #Nested Decision 1
        print("Found some shoes but no battery")
    else:                                                        #If the answer1 is not 'under the bed' this msg will be shown
        print("Found some mess but no battery")

elif question_1 == "in the bathroom":                           #Second Decision
    answer_2 = input("Where in the bathroom should I look? \n") #If the answer2 is 'in the bathtub' the second nested decision will start
    if answer_2 == "in the bathtub":                            #Nested Decision 2
        print("Found a rubber duck but no battery")
    else:                                                       #If the answer2 is not 'in the bathtub' this msg will be shown
        print("Found a wet surface but no battery")

elif question_1 == "in the lab":                                #Third Decision
    answer_3 = input("Where in the lab should I look? \n")      #If the answer3 is 'on the table' the third nested decision will start
    if answer_3 == "on the table":                              #Nested Decision 3
        print("Yes! I found my battery!")
    else:                                                       #If answer3 is not 'on the table' this msg will be shown
        print("Found some tools but no battery.")
else:
    print("I do not know where that is but I will keep looking\n") #In the case that none of the first 3 decisions
                                                                   #are being fulfilled, this msg will be displayed