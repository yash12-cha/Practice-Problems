# Brute Force Approach
def findPeakGrid(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows):
        for j in range(cols):
            current = matrix[i][j]

            # Check the top neighbor
            if i > 0 and matrix[i - 1][j] > current:
                continue  # Not a peak

            # Check the bottom neighbor
            if i < rows - 1 and matrix[i + 1][j] > current:
                continue  # Not a peak

            # Check the left neighbor
            if j > 0 and matrix[i][j - 1] > current:
                continue  # Not a peak

            # Check the right neighbor
            if j < cols - 1 and matrix[i][j + 1] > current:
                continue  # Not a peak

            # If none of the neighbors are greater, current is a peak
            return i,j

    return -1,-1  # No peak found

mat = [[1,4],[3,2]]
ans = findPeakGrid(mat)

'''
Time Complexity:
In the linear search approach, the algorithm examines each element in the matrix to determine if it's a peak.

Worst-case scenario: The algorithm checks every element in the matrix.

Time complexity: O(m × n), where m is the number of rows and n is the number of columns in the matrix.

This is because, in the worst case, the algorithm might need to inspect all elements to find a peak.

Space Complexity:
The algorithm uses a constant amount of extra space:

Variables: Loop indices and a few temporary variables for comparisons.

No additional data structures: It doesn't utilize any extra data structures like stacks, queues, or auxiliary matrices.

Space complexity: O(1)

This means the algorithm's space usage doesn't grow with the size of the input matrix.
'''


# Optimal Approach
def findPeakGrid(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    low = 0
    high = cols - 1

    while low <= high:
        mid_col = (low + high) // 2

        # Find the row index with the maximum value in the middle column
        max_row = 0
        for row in range(rows):
            if matrix[row][mid_col] > matrix[max_row][mid_col]:
                max_row = row

        # Compare with left and right neighbors if they exist
        left = matrix[max_row][mid_col - 1] if mid_col - 1 >= 0 else float('-inf')
        right = matrix[max_row][mid_col + 1] if mid_col + 1 < cols else float('-inf')

        # If the middle column has the peak
        if matrix[max_row][mid_col] >= left and matrix[max_row][mid_col] >= right:
            return (max_row, mid_col)

        # If left neighbor is greater, move to the left half
        elif left > matrix[max_row][mid_col]:
            high = mid_col - 1
        # Else move to the right half
        else:
            low = mid_col + 1

    return (-1, -1)  # No peak found (edge case, should not happen with valid input)

mat = [[10,20,15],[21,30,14],[7,16,32]]
ans = findPeakGrid(mat)

'''
🔍 Time Complexity: O(m × log n)
Where:

m = number of rows

n = number of columns

Breakdown:
The algorithm performs a binary search on columns, which takes O(log n) steps.

In each step, it scans the entire column to find the maximum element in that column, which takes O(m) time.

So total time = O(m) per step × O(log n) steps = O(m × log n)

📦 Space Complexity: O(1)
The algorithm uses a constant amount of extra space (a few variables: low, high, mid_col, etc.).

No additional data structures like arrays or stacks are used.

Hence, space complexity = O(1)
'''