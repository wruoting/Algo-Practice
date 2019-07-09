
def partition(A, p, r):
    i = p-1
    for j in range(p, r+1):
        if A[r] > A[j]:
            i = i+1
            temp = A[j]
            A[j] = A[i]
            A[i] = temp
    temp = A[i+1]
    A[i+1] = A[r]
    A[r] = temp

    return i+1


def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q-1)
        quicksort(A, q+1, r)
    return A


A = [3,4,7,1,2,3,5,6]
print(A)
print(quicksort(A,0,len(A)-1))
