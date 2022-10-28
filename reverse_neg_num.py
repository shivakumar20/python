x = int(input("Enter the negative num : "))

x = abs(x)

x = str(x) + '-'

x = int(x[::-1])

print(f"After reverse : {x}")