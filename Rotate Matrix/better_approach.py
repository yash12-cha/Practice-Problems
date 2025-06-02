'''
Approach (Concept of Swapping)
Think of the matrix as layers (like an onion). For each layer, you're rotating 4 elements at a time — top-left goes to top-right, top-right to bottom-right, bottom-right to bottom-left, and bottom-left to top-left. By moving elements in groups of 4, you rotate the entire matrix 90° clockwise in-place, without needing extra space.
'''
def rotate(matrix):
    n = len(matrix)
    for i in range((n + 1) // 2):
        for j in range(n // 2):
            # Start 4-way swaps
            # temp = bottom left
            temp = matrix[n - 1 - j][i]
            # bottom left = bottom right
            matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1]
            # bottom right = top right
            matrix[n - 1 - i][n - j - 1] = matrix[j][n - 1 - i]
            # top right = top left
            matrix[j][n - 1 - i] = matrix[i][j]
            # top left = temp
            matrix[i][j] = temp
    return matrix

matrix = [[1,2,3],[4,5,6],[7,8,9]]
ans = rotate(matrix)

'''
✅ Why these ranges?
1. for i in range((n + 1) // 2):
We iterate half the rows, because after swapping the top half, the bottom half is already in place.

+1 is used to handle odd-sized matrices (e.g., 3×3), so the middle element in a row is handled correctly.

2. for j in range(n // 2):
We only go through half the columns, for the same reason — one side handles both during the 4-way rotation.

No +1 here because in an odd-sized matrix, the center column doesn’t need to move.
'''

'''
✅ Time Complexity: O(n²)

The nested loops run over approximately half of the matrix:
-> Outer loop runs for ⌈n/2⌉ rows
-> Inner loop runs for ⌊n/2⌋ columns
Despite appearing to do less work, every element still participates in exactly one swap among a 4-way group — covering the entire matrix once.
So, the number of operations is proportional to all n² elements.

✅ Space Complexity: O(1)

The rotation is done in-place, meaning it does not use any extra matrix or list — only a temp variable for swapping.
No additional space scales with input size.
'''