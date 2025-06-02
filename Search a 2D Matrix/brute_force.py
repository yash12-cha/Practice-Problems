'''
Algorithm / Intuition:
The extremely naive approach is to get the answer by checking all the elements of the given matrix. So, we will traverse the matrix and check every element if it is equal to the given ‘target’.
'''
def searchMatrix(matrix, target):
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == target:
                return True
    return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
ans = searchMatrix(matrix, target)

'''
Time Complexity: O(N X M), where N = given row number, M = given column number.
Reason: In order to traverse the matrix, we are using nested loops running for n and m times respectively.

Space Complexity: O(1) as we are not using any extra space.
'''

