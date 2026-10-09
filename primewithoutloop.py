def is_prime(number, divisor=2):
    if number < 2:
        return False

    if divisor * divisor > number:
        return True

    if number % divisor == 0:
        return False

    return is_prime(number, divisor + 1)


number = int(input("Enter a number: "))

if is_prime(number):
    print("Prime number")
else:
    print("Not a prime number")