def movements():
    path = []
    pop = ['Move Forward', 10, 'Move Backwards', 5, 'Move Left', 3, 'Move Right', 1]
    for i in pop:                               #Will append every element of the pop list into the path list
        path.append(i)
    return path

def run():
    print('Moving...')
    x = movements()
    for i in range(1,len(x),2):                 #Decided to use a loop with a 2 as a step to iterate the list
        print(f'{x[i-1]} for {x[i]} steps')     #as a pair of 2 elements, and because I had to start from index1
                                                #which is the second element, I added i-1 as the first index
run()                                           #of the path list from the movements function