#1)
i = 1
while i <= 10:
    print(i)
    i += 1
#2)
i = 10
while i >= 1:
    print(i)
    i -= 1
#3)
i = 2
while i <= 20:
    print(i)
    i += 2
#4)
i = 1
while i <= 20:
    print(i)
    i += 2
#5)
n = int(input("Enter N: "))
total_sum = 0
i = 1

while i <= n:
    total_sum += i
    i += 1

print(f"Sum: {total_sum}")
#6)
num = int(input("Enter a number: "))
i = 1

while i <= 10:
    print(f"{num} x {i} = {num * i}")
    i += 1
#7)
num = int(input("Enter a number: "))
factorial = 1
i = 1

while i <= num:
    factorial *= i
    i += 1

print(f"Factorial: {factorial}")
#8)
num = int(input("Enter a number: "))
reversed_num = 0

while num > 0:
    digit = num % 10
    reversed_num = (reversed_num * 10) + digit
    num //= 10

print(f"Reversed: {reversed_num}")
#9)
num = int(input("Enter a number: "))
original = num
reversed_num = 0

while num > 0:
    digit = num % 10
    reversed_num = (reversed_num * 10) + digit
    num //= 10

if original == reversed_num:
    print("It is a Palindrome number")
else:
    print("It is not a Palindrome number")
#10)
num = int(input("Enter a number: "))
digit_sum = 0
digit_product = 1

while num > 0:
    digit = num % 10
    digit_sum += digit
    digit_product *= digit
    num //= 10

if digit_sum == digit_product:
    print("It is a Spy number")
else:
    print("It is not a Spy number")
