import math
# Merge sort implementation
# This should take 2N+2 where N is the number of elements in A
def merge(A, p, q, r):
    L = list()
    R = list()
    for i in range(p, q+1):
        L.append(A[i])
    for j in range(q+1, r+1):
        R.append(A[j])
    L.append(max(A)+1)
    R.append(max(A)+1)
    for k in range(p, r+1):
        if L[0] >= R[0]:
            A[k] = R[0]
            R.pop(0)
        elif L[0] < R[0]:
            A[k] = L[0]
            L.pop(0)
    return A

def merge_sort(A, p, r):
    if p<r:
        q = int(math.floor((r+p)/2))
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        merge(A,p,q,r)
    return A
A = [25, 1, 5, 7, 12, 38, 3, 18, 21, 23, 25, 32]
print(merge_sort(A, 0, len(A)-1))
