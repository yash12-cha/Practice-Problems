# Brute Force Approach
def searchMatrix(matrix, target):
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == target:
                return True
    return False

matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5
ans = searchMatrix(matrix, target)

'''
Time Complexity: O(N X M), where N = given row number, M = given column number.
Reason: In order to traverse the matrix, we are using nested loops running for n and m times respectively.

Space Complexity: O(1) as we are not using any extra space.
'''

# Another Approach

def binarySearchRow(row, target):
    start = 0
    end = len(row) - 1

    while start <= end:
        mid = (start + end) // 2

        if row[mid] == target:
            return True
        elif row[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return False

def searchMatrix(matrix, target):
    for row in matrix:
        if binarySearchRow(row, target):
            return True
    return False

matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5
ans = searchMatrix(matrix, target)

'''
Time Complexity: O(N*logM), where N = given row number, M = given column number.
Reason: We are traversing all rows and it takes O(N) time complexity. And for all rows, we are applying binary search. So, the total time complexity is O(N*logM).

Space Complexity: O(1) as we are not using any extra space.
'''

# Optimal Approach

def searchMatrix(matrix, target):
    rows = len(matrix)
    cols = len(matrix[0])

    # Start from the top-right corner
    row = 0
    col = cols - 1

    # Move either left or down depending on the comparison
    while row < rows and col >= 0:
        current = matrix[row][col]

        if current == target:
            return True
        elif current < target:
            row += 1  # Move down to a larger element
        else:
            col -= 1  # Move left to a smaller element

    # Target not found
    return False

matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5
ans = searchMatrix(matrix, target)

'''
Time Complexity: O(N+M), where N = given row number, M = given column number.
Reason: We are starting traversal from (0, M-1), and at most, we can end up being in the cell (M-1, 0). So, the total distance can be at most (N+M). So, the time complexity is O(N+M).

Space Complexity: O(1) as we are not using any extra space.
'''