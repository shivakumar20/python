import math


def primefactor(num):
    while num % 2 == 0:
        print(2,end="")
        print("*",end ='')
        num = num / 2

    for i in range(3,int(math.sqrt(num))+1,2):

        while num % i == 0:
            print(i,end="")
            print("*",end ='')
            num = num / i

    if num > 2:
        print(int(num),end = "")

num = int(input("Enter the num : "))
primefactor(num)