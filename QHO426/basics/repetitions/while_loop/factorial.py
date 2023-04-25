number = int(input("Please enter a number: "))
factorial = 0
total = 1

while(factorial < number):      #Until the loop repetition is less than the number requested by user, the total will be updated
    total = total * (number-factorial)      #The total value will be the previous total * the number -1, which represents the next operation of the factorial number
    factorial += 1
print(total)