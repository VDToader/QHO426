a_cable = int(input("How many live cables must I avoid? : "))
l_cable = 0

while (l_cable < a_cable):
    print(f"Avoiding...Done! {l_cable + 1} live cables avoided  ", end="")
    l_cable += 1

print("\nAll live cables have been avoided!")
