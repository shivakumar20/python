def dec_bin(num):
    bin = []

    i = 0
    while num != 0:
        bin.insert(0,(num % 2))

        num = num // 2

    return bin

num = int(input("Enter the number : "))

bin = dec_bin(num)

print(''.join(str(x) for x in bin))


