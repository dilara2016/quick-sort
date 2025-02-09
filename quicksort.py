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


A=[8,17,22,12,0,9,16]
print("Unsorted Array: ")
print(A)

n = len(A) - 1
quicksort(A,0,n)

print("Sorted Array: ")
print(A)