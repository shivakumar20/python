num1 = int(input("Enter num1 : "))
num2 = int(input("Enter num2 : "))

max = num1 if num1>num2 else num2
lim = num1 * num2

for i in range(max,lim + 1,max):
    if (i % num1 == 0) and (i % num2 == 0):
        print(f"The LCM of given numbers : {i} ")
        break