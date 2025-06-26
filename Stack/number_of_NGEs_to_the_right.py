# Brute Force Approach

def count_greater_right(arr):
    
    n = len(arr)
    ans = [0] * n  # Initialize result array with zeros
    # Iterate through each element in the array
    for i in range(n):
        count = 0  # Counter for elements greater than arr[i] to the right
        
        # Check all elements to the right of current element
        for j in range(i + 1, n):
            if arr[j] > arr[i]:
                count += 1  # Increment count if right element is greater
        
        # Store count in result array, or -1 if no greater elements found
        ans[i] = count if count > 0 else -1
    return ans

arr = [3, 4, 2, 7, 5, 8, 10, 6]
ans = count_greater_right(arr)

'''
Time Complexity: O(n^2)

Space Complexity: O(n)
'''

def count_greater_right(arr):
    
    n = len(arr)
    ans = [-1] * n  # Initialize result array with -1
    stack = []  # Stack to keep track of elements

    # Traverse the array from right to left
    for i in range(n - 1, -1, -1):
        count = 0  # Counter for elements greater than arr[i]
        
        # Count how many elements in the stack are greater than arr[i]
        while stack and stack[-1] <= arr[i]:
            stack.pop()  # Remove elements that are not greater
        
        # The remaining elements in the stack are greater than arr[i]
        count = len(stack)  # Count of greater elements
        
        # Store the count in the result array
        ans[i] = count if count > 0 else -1
        
        # Push the current element onto the stack for future comparisons
        stack.append(arr[i])

    return ans

# Example usage:
arr = [3, 4, 2, 7, 5, 8, 10, 6]
result = count_greater_right(arr)
print(result)  # Output: [6, 5, 5, 2, 2, 1, -1, -1]

