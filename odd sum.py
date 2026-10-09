
n = int(input("Enter a number:"))
if n % 2 == 0:
    print(n, "is even")
else:
    print(n, "is odd")
i = 1
j = 0
while i <= n:
    if i % 2 != 0:
        j = j + i
    i = i + 1

print("Sum of odd numbers is", j)