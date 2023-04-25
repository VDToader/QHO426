bars = int(input("How many bars we should charge? : "))
bars_charged = 0
while (bars_charged < bars):
    print("Charging: " + (bars_charged+1)*"█")  #Added bars_charged+1 to show at least one symbol when the charged value outside the loop is 0
    bars_charged += 1
print("\nThe battery is fully charged.")