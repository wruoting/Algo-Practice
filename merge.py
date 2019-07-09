import math
# Merge sort implementation
# This should take 2N+2 where N is the number of elements in A


def merge(A, p, q, r):
    left = list()
    right = list()
    for i in range(p, q+1):
        left.append(A[i])
    left.append(max(A)+1)
    for j in range(q+1, r+1):
        right.append(A[j])
    right.append(max(A)+1)
    for i in range(p, r+1):
        if left[0] < right[0]:
            A[i] = left[0]
            left.pop(0)
        elif left[0] > right[0]:
            A[i] = right[0]
            right.pop(0)
        elif left[0] == right[0]:
            if left[0] != max(A)+1 and right[0] != max(A)+1:
                A[i] = left[0]
                left.pop(0)
    return A


def merge_sort(A, p, r):
    q = int(math.floor((p+r)/2))
    if p < r:
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        merge(A, p, q, r)
    return A

A = [25, 1, 5, 7, 12, 38, 3, 18, 21, 23, 25, 32]
print(merge_sort(A, 0, len(A)-1))
