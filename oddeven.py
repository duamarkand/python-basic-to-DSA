start=int(input("Enter a number Starting range:  "))
end=int(input("Enter another number Ending range: "))

while(start<=end):
    if(start%2==0):
        print(start, "is even")
    else:
        print(start, "is odd")
    start=start+1