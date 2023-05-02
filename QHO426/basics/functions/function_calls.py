def box(ans):
    print(f"-----\n| {ans}  |\n|    |\n-----")

def lower_case(ans):
    print(ans.lower())
def upper_case(ans):
    print(ans.upper())

def mirror(ans):
    print(ans[::-1])

def repeat(ans,times):
    times = int(input("How many times should I display the word ?  : "))
    count = 0
    if times % 2 == 0 and count < times:
        print(ans.upper())
    elif times % 2 == 1 and count < times:
        print(ans.lower())

def run():
    ans = input("Please insert a word: ")
    print("\nPlease choose one of the following options: \n1.Display in a box \n2.Display Lower-case \n3.Display Upper-case \n4.Display Mirrored \n5.Repeat ")
    choice = int(input())
    if choice == 1:
        box(ans)
    elif choice == 2:
        lower_case(ans)
    elif choice == 3:
        upper_case(ans)
    elif choice == 4:
        mirror(ans)
    elif choice == 5:
        repeat(ans)
run()
