def directions():                       #FIrst function is created
    directions = []                     #Empty list that needs to be populated
    directions.append('Move Forward')   #Each append method will add an item to the empty list
    directions.append('Move Backwards')
    directions.append('Turn Left')
    directions.append('Turn Right')
    print(directions)

def run():                              #The second list is created with the sole purpose to call the first one
    directions()

run()                                   #To print the list we need to call the second function
