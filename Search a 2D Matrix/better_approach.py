'''
Approach:
Instead of searching each column sequentially, we can efficiently apply Binary Search on each row to determine if the target is present. 
'''
def searchMatrix(matrix, key):
    n = len(matrix)        # Number of rows
    m = len(matrix[0])     # Number of columns
    
    i = 0                  # Start from the top-right corner
    j = m - 1

    while i < n and j >= 0:
        if matrix[i][j] == key:
            return True
        elif matrix[i][j] > key:
            j -= 1
        else:
            i += 1

    return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
ans = searchMatrix(matrix, target)

'''
Time Complexity: O(N + logM), where N = given row number, M = given column number.
Reason: We are traversing all rows and it takes O(N) time complexity. But for all rows, we are not applying binary search rather we are only applying it once for a particular row. That is why the time complexity is O(N + logM) instead of O(N*logM).

Space Complexity: O(1) as we are not using any extra space.
'''