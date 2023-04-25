num_sum = int(input("How many numbers should I sum up? : "))
total_numbers = 0       #total_numbers variable will count the times that the while loop ran/ after each run its value will be increased by 1 until it will be lower than the number of times requested by the user
total = 0               #total variable used to keep the sum of the numbers updated
while (total_numbers < num_sum):
    print(f"Please enter the number:{total_numbers + 1} of {num_sum}", end=" - ") #added +1 only not to show the "zero" number of num_sum
    number = int(input())
    total = total + number
    total_numbers += 1
print(f"The answer  is : {total}")