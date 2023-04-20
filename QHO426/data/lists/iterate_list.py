def direction():
    directions = []
    directions.append('Move Forward')
    directions.append('Move Backward')
    directions.append('Turn Left')
    directions.append('Turn Right')
    return directions                   #Tbis function will return a populated list with 4 items

def menu():
    print('Please select a direction:')
    x = direction()
    for item in x:
        print(f'{x.index(item)}: {item}')   #For each of the index value, will print it's position and element

def run():
    menu()

run()