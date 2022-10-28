num1 = int(input("Enter num1 : "))
num2 = int(input("Evter num2 : "))

while num1 != num2:
    if num1 > num2:
        num1 = num1 - num2
    else:
        num2 = num2 - num1

print(f"The HCF is : {num1}")