# Brute Force Approach

def markRow(matrix, n, m, i):
    # Set all non-zero elements in row i to -infinity
    # This marks the row for zeroing out later
    for j in range(m):
        if matrix[i][j] != 0:
            matrix[i][j] = -float('inf')

def markCol(matrix, n, m, j):
    # Set all non-zero elements in column j to -infinity
    # This marks the column for zeroing out later
    for i in range(n):
        if matrix[i][j] != 0:
            matrix[i][j] = -float('inf')

def setZeroes(matrix):
    # Get the dimensions of the matrix
    n = len(matrix)  # Number of rows
    m = len(matrix[0])  # Number of columns
    
    # First pass: Identify all rows and columns that need to be zeroed
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                # If a zero is found, mark the entire row and column
                markRow(matrix, n, m, i)
                markCol(matrix, n, m, j)
    
    # Second pass: Set all marked elements (-infinity) to zero
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == -float('inf'):
                matrix[i][j] = 0  # Replace the marker with zero
    
    # The function modifies the matrix in place and does not return anything
    return matrix

matrix = [[1,1,1],[1,0,1],[1,1,1]]
ans = setZeroes(matrix)

'''
Time Complexity: O((N*M)*(N + M)) + O(N*M), where N = no. of rows in the matrix and M = no. of columns in the matrix.
Reason: Firstly, we are traversing the matrix to find the cells with the value 0. It takes O(N*M). Now, whenever we find any such cell we mark that row and column with -1. This process takes O(N+M). So, combining this the whole process, finding and marking, takes O((N*M)*(N + M)).
Another O(N*M) is taken to mark all the cells with -1 as 0 finally.

Space Complexity: O(1) as we are not using any extra space.
'''

# Better Approach

def markRow(matrix, n, m, i):
    # Mark all non-zero elements in row i with -1
    # This indicates that the entire row should be zeroed later
    for j in range(m):
        if matrix[i][j] != 0:
            matrix[i][j] = -1

def markCol(matrix, n, m, j):
    # Mark all non-zero elements in column j with -1
    # This indicates that the entire column should be zeroed later
    for i in range(n):
        if matrix[i][j] != 0:
            matrix[i][j] = -1

def setZeroes(matrix):
    # Get the dimensions of the matrix
    n = len(matrix)  # Number of rows
    m = len(matrix[0])  # Number of columns
    
    # Arrays to keep track of which rows and columns need to be zeroed
    rows_to_mark = [0] * n  # Initialize a list for rows
    cols_to_mark = [0] * m  # Initialize a list for columns
    
    # First pass: Identify rows and columns that need to be zeroed
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                # If a zero is found, mark the corresponding row and column
                rows_to_mark[i] = 1
                cols_to_mark[j] = 1
                markRow(matrix, n, m, i)  # Mark the entire row
                markCol(matrix, n, m, j)  # Mark the entire column

    # Second pass: Set the marked rows and columns to zero
    for i in range(n):
        for j in range(m):
            if rows_to_mark[i] or cols_to_mark[j]:
                # If the row or column is marked, set the element to zero
                matrix[i][j] = 0
    
    # Return the modified matrix
    return matrix

matrix = [[1,1,1],[1,0,1],[1,1,1]]
ans = setZeroes(matrix)

'''
Time Complexity: O(2*(N*M)), where N = no. of rows in the matrix and M = no. of columns in the matrix.
Reason: We are traversing the entire matrix 2 times and each traversal is taking O(N*M) time complexity.

Space Complexity: O(N) + O(M), where N = no. of rows in the matrix and M = no. of columns in the matrix.
Reason: O(N) is for using the row array and O(M) is for using the col array.
'''