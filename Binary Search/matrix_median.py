# Brute Force Approach

def median(matrix):
        m = len(matrix)
        n = len(matrix[0])
        lst = []  # Initialize an empty list to store matrix elements
    
        # Traverse the matrix and copy the elements to the list
        for i in range(m):
            for j in range(n):
                lst.append(matrix[i][j])  # Append each element to the list
    
        # Sort the list to find the median
        lst.sort()
    
        # Calculate the median index
        median_index = (m * n) // 2
        # If the total number of elements is odd, return the middle element
        if (m * n) % 2 == 1:
            return lst[median_index]
        else:
            # If even, return the average of the two middle elements
            return (lst[median_index - 1] + lst[median_index]) / 2


matrix = [[1, 3, 5], [2, 6, 9], [3, 6, 9]]
ans = median(matrix)

'''
Time Complexity: O(m * n) + O(m * n(log(m * n))), where m = number of row in the given matrix, n = number of columns in the given matrix

Reason: At first, we are traversing the matrix to copy the elements. This takes O(m * n) time complexity. Then we are sorting the linear array of size (m * n), that takes O(m * n(log(m * n))) time complexity

Space Complexity: O(m * n) as we are using a temporary list to store the elements of the matrix.
'''

# Optimal Approach

def upperBound(arr, target):

    n = len(arr)
    low = 0
    high = n - 1
    ans = n  # Default answer is n (out of bounds)

    # Perform binary search to find the upper bound
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] <= target:
            low = mid + 1  # Look on the right side
        else:
            ans = mid  # Potential answer found
            high = mid - 1  # Look for a smaller index on the left

    return ans

def blackBox(matrix, x):

    cnt = 0
    for i in range(len(matrix)):
        cnt += upperBound(matrix[i], x)  # Count elements in each row
    return cnt

def findMedian(matrix):
    
    n = len(matrix)  # Number of rows
    m = len(matrix[0])  # Number of columns
    low = float('inf')  # Initialize low to positive infinity
    high = float('-inf')  # Initialize high to negative infinity

    # Find the minimum and maximum values in the matrix
    for i in range(n):
        low = min(low, matrix[i][0])  # First element of each row
        high = max(high, matrix[i][m - 1])  # Last element of each row

    required = (n * m) // 2  # Calculate the required count for median

    # Binary search to find the median
    while low <= high:
        mid = (low + high) // 2  # Midpoint value
        smaller_equals = blackBox(matrix, mid)  # Count elements <= mid

        if smaller_equals <= required:
            low = mid + 1  # Move to the right half
        else:
            high = mid - 1  # Move to the left half

    return low  # The median value

matrix = [[1, 3, 5], [2, 6, 9], [3, 6, 9]]
ans = findMedian(matrix)

'''
Time Complexity: O(log(10^9)) X O(m(log n)), where m = number of rows in the given matrix, n = number of columns in the given matrix

Reason: Our search space lies between [0, 10^9] as the min(matrix) can be 0 and the max(matrix) can be 10^9. We are applying binary search in this search space and it takes O(log(10^9)) time complexity. Then we call countSmallEqual() function for every ‘mid’ and this function takes O(m(log n)) time complexity.

Space Complexity : O(1) as we are not using any extra space
'''