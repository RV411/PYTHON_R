def isPossibleTriangle (arr , N):
     
    # If number of elements
    # are less than either 3 or 9, then
    # no triangle is possible
    if N < 3 | N > 9:
        return False
     
    # first sort the array
    arr.sort()
     
    # loop for all 3
    # consecutive triplets
    for i in range(N - 2):
         
        # If triplet satisfies triangle
        # condition, break
        if arr[i] + arr[i + 1] > arr[i + 2]:
            return True
    
def main():
    # Driver Code
    arr = [5, 4, 3, 1, 2]
    N = len(arr)
    print("Yes" if isPossibleTriangle(arr, N) else "No")
        
main()
        # This code is contributed
        # by "Sharad_Bhardwaj".