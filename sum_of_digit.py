x = int(input("Enter the number : "))
y = x
sum = 0
while x != 0:

    sum = sum + (x%10)

    x = x//10

print(f'The sum of number {y} : {sum}')