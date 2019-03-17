def partition(A, p, r):
	i = p - 1
	for j in range(p,r+1):
		if A[j] < A[r]:
			temp = A[j]
			i = i+1
			A[j] = A[i]
			A[i] = temp
	temp = A[r]
	A[r] = A[i]
	A[i] = temp
	return i+1

def quicksort(A, p, r):
	if p < r:
		q = partition(A, p, r)
		quicksort(A,p,q)
		quicksort(A,q+1,r)
	return A

A = [3,4,7,1,2,3,5,6]
print(A)
print(partition(A,0,len(A)-1))
