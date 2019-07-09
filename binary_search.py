import math
def binarySearch(x, A, index):
    if A[index] == x:
        return index
    if index != 1:
        if A[index] > x:
            new_index = int(math.floor(index/2))
            return binarySearch(x, A, new_index)
        elif A[index] < x:
            new_index = int(math.floor(index * 3/2))
            return binarySearch(x, A, new_index)
    else:
        return -1

        
        
# Test array 
arr = [ 2, 3, 4, 5, 6, 7, 10, 15, 20, 25, 30, 40 ] 
x = 10
  
# Function call 
result = binarySearch(x, arr, int(math.floor(len(arr))/2))
print(result) 
  