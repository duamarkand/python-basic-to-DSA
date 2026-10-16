# Program to swap two numbers without using a third variable

a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))

print(f"\nBefore swap: a = {a}, b = {b}")

# Swap using arithmetic operators (+ and -)
a = a + b  # Sum of both numbers
b = a - b  # (a + b) - b = original a
a = a - b  # (a + b) - original a = original b

print(f"After swap:  a = {a}, b = {b}")

