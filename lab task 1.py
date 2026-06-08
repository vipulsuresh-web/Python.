'''#1)getting two numbers from user
A=int(input("Enter value of A:"))
B=int(input("Enter value of B:"))
#i)ADDITON
print("Addition:",A+B)
#ii)SUBRACTION
print("Subraction:",A-B)
#iii)MULTIPLICATION
print("Multiplication:",A*B)
#iv)DIVISON
print("Division:",A/B)
#v)MODULUS(REMINDER)
print("Modulus:",A%B)
#vi)FLOOR DIVISION
print("Floor_Division:",A//B)
#vii)EXPONENTATION
print("Exponentation:",A**B)

#2)Write a program to calculate the area and perimeter of a rectangle,square and circle
#Area,perimeter of rectangle,square
L=int(input("Enter value of Length:"))
B=int(input("Enter value of Bredth:"))
print("Perimeter of Rectangle:",2*(L+B))
print("Area of Rectangle:",L*B)
#Perimeter,area of circle
R=int(input("Enter value of radius:"))
print("perimeter of circle:",2*3.14*R)
print("area of circle:",    3.14*R**2)
L=int(input("Enter value of Length:"))
print("perimetre of square:",4*L)
print("Area of square:",L**2)

#3)
A=int(input("Enter 1st number:"))
B=int(input("Enter 2nd number:"))
C=int(input("Enter 3rd number:"))
print("Average of 3 numbers:",(A+B+C)/3)'''

#4)
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

# i) If two numbers are equal
if a == b:
    print("The numbers are equal.")
else:
    print("The numbers are not equal.")

# ii) If one number is greater than the other
if a > b:
    print(f"{a} is greater than {b}")
elif b > a:
    print(f"{b} is greater than {a}")

# iii) If a number is less than or equal to another
if a <= b:
    print(f"{a} is less than or equal to {b}")
else:
    print(f"{a} is greater than {b}")
#5)
num = float(input("Enter a number: "))
square_root = num ** 0.5
print(f"The square root of {num} is {square_root}")
#6)
p = float(input("Enter Principal amount: "))
r = float(input("Enter Annual Rate of interest (%): "))
t = float(input("Enter Time (years): "))

# Simple Interest calculation
si = (p * r * t) / 100

# Compound Interest calculation
ci = p * ((1 + r / 100) ** t) - p

print(f"Simple Interest: {si}")
print(f"Compound Interest: {ci}")
#7)
x = 10
x += 5   # x = 15
x -= 3   # x = 12
x *= 2   # x = 24
x /= 4   # x = 6.0
x %= 2   # x = 0.0
x **= 3  # x = 0.0

print(f"Final value of x: {x}")
#8)
a = int(input("Enter a: "))
b = int(input("Enter b: "))

# Swapping without temporary variable
a = a + b
b = a - b
a = a - b

print(f"After swapping: a = {a}, b = {b}")
#9)
num = float(input("Enter a number: "))
cube_root = num ** (1/3)
print(f"The cube root of {num} is {cube_root}")
#10)
num = 8523
# Using modulo 100 extracts the last two digits
last_two_digits = num % 100
print(f"The last 2 digits of {num} are {last_two_digits}")
#11)
num = 8523
# Using integer division (//) removes the last two digits
remaining_digits = num // 100
print(f"After removing the last 2 digits, we get: {remaining_digits}")














                               





















