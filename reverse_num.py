x = int(input("Enter the number : "))
y = x
rem = 0

rev = 0

while x > 0:
    rem = x % 10
    rev = (rev * 10) + rem
    x = x//10

print(f"Reverse of {y} is : {rev}",end = '')
if y == rev:
    print("  And also a Palindrom ")