'''
Intuition: By observation, we see that the first column of the original matrix is the reverse of the first row of the rotated matrix, so that’s why we transpose the matrix and then reverse each row, and since we are making changes in the matrix itself space complexity gets reduced to O(1).

Approach:

Step 1: Transpose the matrix. (transposing means changing columns to rows and rows to columns)

Step 2: Reverse each row of the matrix.
'''

def transpose(matrix,n, m):
    for i in range(n):
        for j in range(i, m):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix


def reverse(matrix):
    for row in matrix:
        row.reverse()
    return matrix
def rotate(matrix):
    n = len(matrix)
    m = len(matrix[0])
    transpose(matrix, n, m)
    reverse(matrix)
    return matrix

matrix = [[1,2,3],[4,5,6],[7,8,9]]
ans = rotate(matrix)

'''
Time Complexity: O(N*N) + O(N*N).One O(N*N) is for transposing the matrix and the other is for reversing the matrix.

Space Complexity: O(1).
'''