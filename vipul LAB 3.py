#1)
for i in range(1, 11):
    print(i)
#2)
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
#3)
for i in range(2, 51, 2):
    print(i)
#4)
num = int(input("Enter a number: "))
factorial = 1

for i in range(1, num + 1):
    factorial *= i

print(f"Factorial of {num} is {factorial}")
#5)
for i in range(ord('A'), ord('G') + 1):
    print(chr(i))
#6)
for i in range(1, 5):
    print("*" * i)
#7)
for i in range(1, 21, 2):
    print(i)

#8)
size = 5
for i in range(size):
    if i == 0 or i == size - 1:
        print("*" * size)
    else:
        print("*" + " " * (size - 2) + "*")
#9)
rows = 4
for i in range(rows, 0, -1):
    print("*" * i)
#10)
rows = 4
current_number = 1

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(current_number, end=" ")
        current_number += 1
    print()

