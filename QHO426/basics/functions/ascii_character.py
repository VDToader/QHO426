print("Program Started!")
code = int(input ("Please enter an ASCII code: "))
if code in range(32,127): # Added 127 as an end for the range, to include the 126th element
    print(f"The character represented by the ASCII code {code} is {chr(code)}.")
else:
    print("The ASCII code value should be between 32 and 126 included")
print("Program Ended!")