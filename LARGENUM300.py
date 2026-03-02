x = 300

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if abs(num1 - x) <= abs(num2 - x) and abs(num1 - x) <= abs(num3 - x):
    closest = num1
elif abs(num2 - x) <= abs(num1 - x) and abs(num2 - x) <= abs(num3 - x):
    closest = num2
else:
    closest = num3

print("The closest number to", x, "is", closest)