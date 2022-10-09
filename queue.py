'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

queue = []

x = int(input("enter the number of element : "))

for i in range (0,x):
    y = int(input("Enter the element: "))
    queue.append(y)
    
print(f'All the elements in queue : {queue}')

for i in range(0,x):
    
    queue.pop(0)
    
print(f'{queue}')
