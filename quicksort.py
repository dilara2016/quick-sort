def partition(A, low, high):
    pivot = A[high]

    i = low - 1

    for j in range(low, high):
        if A[j] <= pivot:
            i = i+1
            (A[i], A[j], A[i])


    (A[i+1], A[high]) = (A[high], A[i+1])
    return i + 1

def quicksort(A,low,high):
    if  low < high:
        pi = partition(A, low, high)
        quicksort(A,low,pi-1)
        quicksort(A,pi+1,high)


Array_size=int(input("enter size of the array: "))
A=[]
for i in range(Array_size):
    inp = int(input("Enter Element: "))
    A.append(inp)
print("Unsorted Array: ")
print(A)

n = len(A) - 1
quicksort(A,0,n)

print("Sorted Array: ")
print(A)