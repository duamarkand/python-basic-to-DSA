n=int(input("Enter a number: "))
if(n<2):
    is_prime=True
else:
    is_prime=True
    div=2
    while(div*div<=n):
        if(n%div==0):
            is_prime=False
            break
        div=div+1
if(is_prime):
    print(n, "is a prime number")
else:
    print(n, "is not a prime number")   