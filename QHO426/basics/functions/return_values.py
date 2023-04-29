def sum_weights(weight_Bip,weight_Bop):         #The first function will only calculate the total weight for the two bots
    total_weight = weight_Bip + weight_Bop      #and will return the total weight value
    return total_weight

def calc_avg_weight(avg_weight_Bip,avg_weight_Bop):     #The second function will calculate the average weight of the two bots
    avg_weight = (avg_weight_Bip + avg_weight_Bop)/2    #and will return it as a velue stored inside avg_weight variable
    return avg_weight

def run():                                                  #Third and final function will store 2 values inserted by the user each of it representing the
    weight_Bip = int(input("What is the weight of Bip: "))  #bots weight and afterwards it will ask the user to choose an specific action
    weight_Bop = int(input("What is the weight of Bop: "))
    ans = input("What would you like to calculate (sum or average) ? ")
    if ans.lower() == "sum":            #added the lower method just in case the user uses capital letters
        print(f"The sum of Bip and Bop weights is : {sum_weights(weight_Bip,weight_Bop)}")
    elif ans.lower() == "average":
        print(f"The average weight of Bip and Bop is: {calc_avg_weight(weight_Bip,weight_Bop)}")
    else:
        print("You need to choose one of the two possibilities")

run()