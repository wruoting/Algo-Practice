import math
def max_heapify(A, i):
    left = (i+1)*2 - 1
    right = (i+1)*2
    largest = i
    if left < len(A) and A[left] > A[i]:
        largest = left
    if right < len(A) and A[right] > A[i]:
        if largest == left and A[right]> A[left]:
            largest = right
        elif largest == i:
            largest = right
    if largest != i:
        temp = A[largest]
        A[largest] = A[i]
        A[i] = temp
        return max_heapify(A, largest)
    return A
def build_heap(A):
    index = int(math.floor(len(A)/2))-1
    for i in range(index, -1, -1):
        max_heapify(A, i)
    return A

def swim_up(i, A):
    if i>0 and A[i] > A[int(math.floor((i-1)/2))]:
        # swap i and i/2
        temp = A[i]
        A[i] = A[int(math.floor((i-1)/2))]
        A[int(math.floor((i-1)/2))] = temp
        return swim_up(int(math.floor((i-1)/2)), A)
    return A
    
A = [9, 3, 16, 1, 2, 8, 9]
A = [6, 8, 12, 7, 5, 8, 10, 12, 17, 2, 1]
# print(build_heap(A))
# A.pop(0)
print(build_heap(A))

A.append(20)
print(A)
swim_up(len(A)-1, A)
print(A)
