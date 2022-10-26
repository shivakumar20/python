x = int(input("Enter the number : "))

isprime = True

count = 0

if(x < 2):
    isprime = False

else:
    for i in range(2,(x//2)):
        if(x % i == 0):
            isprime = False
            print("Not a Prime number ")
            break
        else:
            count = count + 1

    if count>0:
        print("Prime number")
        