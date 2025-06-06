# Brute Force Approach
def rowAndMaximumOnes(matrix):
    n = len(matrix)
    m = len(matrix[0])
    cnt_max = 0
    index = -1

    # traverse the matrix:
    for i in range(n):
        cnt_ones = sum(matrix[i])
        if cnt_ones > cnt_max:
            cnt_max = cnt_ones
            index = i
    return index

mat = [[0,1],[1,0]]
ans = rowAndMaximumOnes(mat)

'''
Time Complexity: O(n X m), where n = given row number, m = given column number.
Reason: We are using nested loops running for n and m times respectively.

Space Complexity: O(1) as we are not using any extra space.
'''

# Optimal Approach
def lowerBound(arr, n , x):
      low = 0
      high = n - 1
      result = n  # Default to n, meaning no element found
      while low <= high:
          mid = (low + high) // 2
          if arr[mid] >= x:
              result = mid  # Update result to mid
              high = mid - 1  # Move left
          else:
              low = mid + 1  # Move right
      return result
      
def rowMaxOnes(matrix):
    n = len(matrix)
    m = len(matrix[0])
    cnt_max = 0
    index = -1

    # traverse the rows:
    for i in range(n):
        # get the number of 1's:
        cnt_ones = m - lowerBound(matrix[i], m, 1)
        if cnt_ones > cnt_max:
            cnt_max = cnt_ones
            index = i
    return index

mat = [[1, 1, 1], [0, 0, 1], [0, 0, 0]]
ans = rowMaxOnes(mat)

'''
Time Complexity: O(n X logm), where n = given row number, m = given column number.
Reason: We are using a loop running for n times to traverse the rows. Then we are applying binary search on each row with m columns.

Space Complexity: O(1) as we are not using any extra space.
'''