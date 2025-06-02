'''
Approach: Take another dummy matrix of n*n, and then take the first row of the matrix and put it in the last column of the dummy matrix, take the second row of the matrix, and put it in the second last column of the matrix and so.
'''
def rotate(matrix):
    n = len(matrix) # Number of rows
    m = len(matrix[0]) # Number of columns

    # Create a new matrix filled with zeros
    new_matrix = [[0] * m for _ in range(n)]

    # Rotate the matrix
    for i in range(n):
        for j in range(m):
            new_matrix[j][n - 1 - i] = matrix[i][j]

    return new_matrix

matrix = [[1,2,3],[4,5,6],[7,8,9]]
ans = rotate(matrix)

'''
Time Complexity: O(N*N) to linearly iterate and put it into some other matrix.
Space Complexity: O(N*N) to copy it into some other matrix.
'''