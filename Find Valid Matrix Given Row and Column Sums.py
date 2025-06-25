# Brute Force Approach
def restoreMatrix(rowSum, colSum):
    n = len(rowSum)
    m = len(colSum)
    # Initialize an n×m matrix filled with zeros
    matrix = [[0] * m for _ in range(n)]
    
    # Fill each cell greedily
    for i in range(n):
        for j in range(m):
            # Determine the maximum we can place here without exceeding sums
            min_val = min(rowSum[i], colSum[j])
            
            # Place the value
            matrix[i][j] = min_val
            
            # Deduct from available row and column sums
            rowSum[i] -= min_val
            colSum[j] -= min_val
    
    return matrix

rowSum = [3,8]
colSum = [4,7]
ans = restoreMatrix(rowSum, colSum)

'''
Time Complexity: O(n × m)
We iterate over all n rows and m columns exactly once, performing O(1) operations per cell .

Space Complexity: O(n × m)
That's for the output matrix.
'''

# Optimal Approach
def restoreMatrix(rowSum, colSum):
    m, n = len(rowSum), len(colSum)
    # Initialize the result matrix with zeros
    res = [[0] * n for _ in range(m)]
    
    r = 0  # row pointer
    c = 0  # column pointer
    
    # Greedy: fill the matrix by taking the minimum possible for each cell
    while r < m and c < n:
        # Decide how much to put at (r, c) without exceeding rowSum[r] or colSum[c]
        minVal = min(rowSum[r], colSum[c])
        res[r][c] = minVal
        
        # Update the remaining sums
        rowSum[r] -= minVal
        colSum[c] -= minVal
        
        # If this row is satisfied (0 left), move to next row…
        if rowSum[r] == 0:
            r += 1
        # …otherwise, this column is satisfied, move to next column
        else:
            c += 1
            
    return res

rowSum = [3,8]
colSum = [4,7]
ans = restoreMatrix(rowSum, colSum)

'''
Time Complexity: O(n × m)
We iterate over all n rows and m columns exactly once, performing O(1) operations per cell .

Space Complexity: O(n × m)
That's for the output matrix.
'''