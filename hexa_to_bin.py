def hexa_dec(hex):
    length = len(hex)
    pos = 0
    dec = 0
    for i in range(length -1,-1,-1):
        if '0'<=hex[i]<='9':
            dig = ord(hex[i]) - 48
            dec = dec + (dig * (16 ** pos))
            pos = pos + 1

        elif 'A'<=hex[i]<='f':
            dig = ord(hex[i]) - 55
            dec = dec + (dig * (16 ** pos))
            pos = pos + 1
    
    return dec

hex = input("Enter the num : ")
print(hexa_dec(hex))
