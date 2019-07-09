import math
def max_heapify(A, i):
    left = (i+1)*2 - 1
    right = (i+1)*2
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
