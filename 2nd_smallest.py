import math

def sec_smallest(arr):
    smallest = arr[0]

    for i in range(len(arr)):
        if (arr[i] < smallest):
            smallest = arr[i]

    sec_smallest = math.inf

    for i in range(len(arr)):
        if arr[i] != smallest and arr[i]<sec_smallest:
            sec_smallest = arr[i]

    return sec_smallest


n = int(input("Enter the size of array : "))
arr = []
for i in range(n):
    x = int(input(f"Enter {i} : "))
    arr.append(x)

print(f"The 2nd smallest element : {sec_smallest(arr)}")