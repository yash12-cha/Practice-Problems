# Brute Force Approach

def kthElement(nums1, nums2, k):

    # Create an array to hold the merged result
    arr = [0] * (len(nums1) + len(nums2))

    i = 0  # Pointer for nums1
    j = 0  # Pointer for nums2
    p = 0  # Pointer for the merged array

    # Compare and merge the two arrays into arr
    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]:
            arr[p] = nums1[i]  # Add the smaller element to arr
            i += 1  # Move the pointer in nums1
        else:
            arr[p] = nums2[j]  # Add the smaller element to arr
            j += 1  # Move the pointer in nums2
        p += 1  # Move the pointer in the merged array

    # Copy any remaining elements from nums1
    while i < len(nums1):
        arr[p] = nums1[i]  # Add remaining elements to arr
        i += 1  # Move the pointer in nums1
        p += 1  # Move the pointer in the merged array

    # Copy any remaining elements from nums2
    while j < len(nums2):
        arr[p] = nums2[j]  # Add remaining elements to arr
        j += 1  # Move the pointer in nums2
        p += 1  # Move the pointer in the merged array

    return arr[k-1]

a = [2, 3, 6, 7, 9]
b = [1, 4, 8, 10]
k = 5
ans = kthElement(a, b, k)

'''
Time Complexity: O(m+n), where m and n are the sizes of the given arrays.
Reason: We traverse through both arrays linearly.

Space Complexity: O(m+n), where m and n are the sizes of the given arrays.

Reason: We are using an extra array of size (m+n) to solve this problem.
'''

# Better Approach

def kthElement(a, b, k):
    m = len(a)
    n = len(b)
    ele = -1  # Variable to store the k-th element
    cnt = 0  # Counter to track the number of elements processed

    # Initialize pointers for both arrays
    i, j = 0, 0

    # Merge step: Compare elements from both arrays
    while i < m and j < n:
        if a[i] < b[j]:
            # If the current element from a is smaller
            if cnt == k - 1:
                ele = a[i]  # Found the k-th element
            cnt += 1  # Increment the counter
            i += 1  # Move to the next element in a
        else:
            # If the current element from b is smaller or equal
            if cnt == k - 1:
                ele = b[j]  # Found the k-th element
            cnt += 1  # Increment the counter
            j += 1  # Move to the next element in b

    # Copy any remaining elements from array a
    while i < m:
        if cnt == k - 1:
            ele = a[i]  # Found the k-th element
        cnt += 1  # Increment the counter
        i += 1  # Move to the next element in a

    # Copy any remaining elements from array b
    while j < n:
        if cnt == k - 1:
            ele = b[j]  # Found the k-th element
        cnt += 1  # Increment the counter
        j += 1  # Move to the next element in b

    return ele  # Return the k-th smallest element


a = [2, 3, 6, 7, 9]
b = [1, 4, 8, 10]
k = 5
ans = kthElement(a, b, k)

'''
Time Complexity: O(m+n), where m and n are the sizes of the given arrays.
Reason: We traverse through both arrays linearly.

Space Complexity: O(1), as we are not using any extra space to solve this problem.
'''

def kthElement(nums1, nums2, k):
    
    # Ensure nums1 is the smaller array for efficient binary search
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    m, n = len(nums1), len(nums2)  # Get lengths of both arrays
    left = k  # Length of the left half to consider

    # Initialize binary search bounds
    low = max(0, k - n)  # Lower bound for mid1
    high = min(k, m)  # Upper bound for mid1

    # Perform binary search to find the correct partition
    while low <= high:
        mid1 = (low + high) // 2  # Partition index in nums1
        mid2 = left - mid1  # Partition index in nums2

        # Initialize left and right boundary values for both partitions
        l1 = float('-inf')  # Left max of nums1
        l2 = float('-inf')  # Left max of nums2
        r1 = float('inf')   # Right min of nums1
        r2 = float('inf')   # Right min of nums2

        # Update r1 if mid1 is within bounds
        if mid1 < m:
            r1 = nums1[mid1]
        # Update r2 if mid2 is within bounds
        if mid2 < n:
            r2 = nums2[mid2]
        # Update l1 if mid1 is greater than 0
        if mid1 - 1 >= 0:
            l1 = nums1[mid1 - 1]
        # Update l2 if mid2 is greater than 0
        if mid2 - 1 >= 0:
            l2 = nums2[mid2 - 1]

        # Check if we have found the correct partition
        if l1 <= r2 and l2 <= r1:
            return max(l1, l2)  # Return the k-th smallest element

        # Eliminate the halves based on the partition values
        elif l1 > r2:
            high = mid1 - 1  # Move left in nums1
        else:
            low = mid1 + 1  # Move right in nums1

a = [2, 3, 6, 7, 9]
b = [1, 4, 8, 10]
k = 5
ans = kthElement(a, b, k)

'''
Time Complexity: O(log(min(m, n))), where m and n are the sizes of two given arrays.
Reason: We are applying binary search on the range [max(0, k-n2), min(k, n1)]. The range length <= min(m, n).

Space Complexity: O(1), as we are not using any extra space to solve this problem.
'''