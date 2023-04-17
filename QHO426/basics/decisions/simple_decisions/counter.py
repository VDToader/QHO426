first = int(input("Please enter the first number.\n"))
second = int(input("Please enter the second number.\n"))
third = int(input("Please enter the third number.\n"))
odd_counter = 0     #added 2 counters to keep tracking the odd/even true conditions
even_counter = 0

if first % 2 == 0:
    even_counter += 1   # The first block will check if the first number is odd or even and will increase the counter with 1
elif first % 2 == 1:
    odd_counter += 1

if second % 2 == 0:
    even_counter += 1   #The second block will check if the second number is odd or even and will increase the counter with 1
elif second % 2 == 1:
    odd_counter += 1

if third % 2 == 0:
    even_counter += 1   #Finally the third block will check if the third number is odd or even and will increase the counter with 1
elif third % 2 == 1:
    odd_counter += 1

print(f"You inserted {odd_counter} odd numbers and {even_counter} even numbers!")  #Will print the value of both counters to check how many numbers were odd or even