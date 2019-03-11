import math
def max_heapify(A, i):
    left_index = 2*(i+1)-1
    right_index = 2*(i+1)

    largest = i
    if left_index < len(A):
        if A[i] < A[left_index]:
            largest = left_index
            temp = A[i]
            A[i] = A[left_index]
            A[left_index] = temp
    if right_index < len(A):
        if A[i] < A[right_index]:
            largest = right_index
            temp = A[i]
            A[i] = A[right_index]
            A[right_index] = temp
    if largest == i:
        return A
    return max_heapify(A, largest)

def build_heap(A):
    for i in range(int(math.floor(len(A)/2)),-1,-1):
        max_heapify(A, i)
    return A

A = [9, 3, 16, 1, 2, 8, 9]
A = [6, 2, 5, 8, 10, 12, 17, 2, 1]
print(build_heap(A))
A.pop(0)
print(build_heap(A))
