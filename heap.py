import math


def max_heapify(A, i):
    left = 2*(i+1)-1
    right = 2*(i+1)
    largest = i
    if left < len(A) and A[left] > A[i]:
        largest = left
    if right < len(A) and A[right] > A[i]:
        if largest == left:
            if A[right] > A[left]:
                largest = right
        else:
            largest = right
    temp = A[largest]
    A[largest] = A[i]
    A[i] = temp

    if largest == i:
        return A
    max_heapify(A, largest)


def build_heap(A):
    q = int(math.floor(len(A)/2))
    for i in range(q, -1, -1):
        max_heapify(A, i)
    return A


A = [9, 3, 16, 1, 2, 8, 9]
A = [6, 8, 12, 7,  5, 8, 10, 12, 17, 2, 1]
print(build_heap(A))
A.pop(0)
print(build_heap(A))
