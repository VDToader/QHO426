def directions():
    directions = []
    li = ['Move Forward', 'Move Backwards', 'Turn Left', 'Turn Right']
    for element in li:
        directions.append(element)
    return directions


def menu():
    directions()
    new_list = directions()
    for element in range(0, len(new_list)):
        print(f'{element}:{new_list[element]}')
    movement = int(input('Select your move:'))
    return new_list[movement]

def run():
    route = []
    print('Working on our escape route...')
    i = 0
    for i in range (0,5):
        route_item = menu()
        route.append(route_item)
        i =+ 1
    print(f'Escape route: {enumerate(route)}')
run()
