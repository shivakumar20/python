def bin_dec(num):
    i = 0
    dec = 0
    while num != 0:
        dig = num % 10
        dec = dec + (dig * (2 ** i))
        num = num // 10
    return dec

num  = int(input("Enter the number : "))

print(bin_dec(num))