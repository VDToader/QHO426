#Celsius to Fahrenheit Converter
print("This is a Celsius Degree converter to Fahrenheit")
celsius = float(input("Degree Celsius : "))
F = celsius * (9/5)+ 32
print(f"{celsius:.2f}°C are {F:.2f}°F")

print("Celsius Degrees :" + ("*" * int(celsius)))
print("Fahrenheit Degrees :" + ("❃" * int(F)))