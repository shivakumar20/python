def oct_dec(num):
    dec = 0
    i = 0
    while num != 0:
        dig = num % 10
        dec = dec + (dig * (8 ** i))
        num = num // 10
        i = i + 1
    return dec

num = int(input("ENter the number: "))

print(oct_dec(num))