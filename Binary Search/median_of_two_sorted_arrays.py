# Brute Force Approach


def findMedianSortedArrays(nums1, nums2):

    # Create an array to hold the merged result
    arr = [0] * (len(nums1) + len(nums2))

    i = 0  # Pointer for nums1
    j = 0  # Pointer for nums2
    k = 0  # Pointer for the merged array

    # Compare and merge the two arrays into arr
    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]:
            arr[k] = nums1[i]  # Add the smaller element to arr
            i += 1  # Move the pointer in nums1
        else:
            arr[k] = nums2[j]  # Add the smaller element to arr
            j += 1  # Move the pointer in nums2
        k += 1  # Move the pointer in the merged array

    # Copy any remaining elements from nums1
    while i < len(nums1):
        arr[k] = nums1[i]  # Add remaining elements to arr
        i += 1  # Move the pointer in nums1
        k += 1  # Move the pointer in the merged array

    # Copy any remaining elements from nums2
    while j < len(nums2):
        arr[k] = nums2[j]  # Add remaining elements to arr
        j += 1  # Move the pointer in nums2
        k += 1  # Move the pointer in the merged array

    # Calculate the total number of elements
    n = len(nums1) + len(nums2)

    # If the total number of elements is odd, return the middle element
    if n % 2 == 1:
        return float(arr[n // 2])

    # If the total number of elements is even, return the average of the two middle elements
    median = (arr[n // 2] + arr[(n // 2) - 1]) / 2.0
    return median  # Return the calculated median


nums1 = [1, 3]
nums2 = [2]
ans = findMedianSortedArrays(nums1, nums2)

"""
Time Complexity: O(n1+n2), where  n1 and n2 are the sizes of the given arrays.
Reason: We traverse through both arrays linearly.

Space Complexity: O(n1+n2), where  n1 and n2 are the sizes of the given arrays.
Reason: We are using an extra array of size (n1+n2) to solve this problem.
"""

# Better Approach


def findMedianSortedArrays(nums1, nums2):

    n1 = len(nums1)  # Length of the first array
    n2 = len(nums2)  # Length of the second array
    n = n1 + n2  # Total length of the combined arrays
    indx1 = (n - 1) // 2  # Index of the first median element
    indx2 = n // 2  # Index of the second median element

    i = 0  # Pointer for nums1
    j = 0  # Pointer for nums2
    cnt = 0  # Counter to track the number of elements processed
    ind1el = -1  # Placeholder for the first median element
    ind2el = -1  # Placeholder for the second median element

    # Merge the two arrays until we reach the median indices
    while i < n1 and j < n2:
        if nums1[i] < nums2[j]:
            if cnt == indx1:
                ind1el = nums1[i]  # Store the first median element
            if cnt == indx2:
                ind2el = nums1[i]  # Store the second median element
            cnt += 1
            i += 1
        else:
            if cnt == indx1:
                ind1el = nums2[j]  # Store the first median element
            if cnt == indx2:
                ind2el = nums2[j]  # Store the second median element
            cnt += 1
            j += 1

    # If there are remaining elements in nums1
    while i < n1:
        if cnt == indx1:
            ind1el = nums1[i]  # Store the first median element
        if cnt == indx2:
            ind2el = nums1[i]  # Store the second median element
        cnt += 1
        i += 1

    # If there are remaining elements in nums2
    while j < n2:
        if cnt == indx1:
            ind1el = nums2[j]  # Store the first median element
        if cnt == indx2:
            ind2el = nums2[j]  # Store the second median element
        cnt += 1
        j += 1

    # If the total number of elements is odd, return the second median element
    if n % 2 == 1:
        return float(ind2el)

    # If the total number of elements is even, return the average of the two median elements
    return (ind2el + ind1el) / 2.0


nums1 = [1, 3]
nums2 = [2]
ans = findMedianSortedArrays(nums1, nums2)

"""
Time Complexity: O(N * (sum(arr)-max(arr)+1)), where N = size of the array, sum(arr) = sum of all array elements, max(arr) = maximum of all array elements.
Reason: We are using a loop from max(arr) to sum(arr) to check all possible values of time. Inside the loop, we are calling the countPartitions() function for each number. Now, inside the countPartitions() function, we are using a loop that runs for N times.

Space Complexity:  O(1) as we are not using any extra space to solve this problem.
"""


# Optimal Approach
def findMedianSortedArrays(nums1, nums2):

    # Always binary-search on the smaller array for faster performance
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1  # Ensure nums1 is the smaller array

    n1, n2 = len(nums1), len(nums2)  # Get lengths of both arrays
    total = n1 + n2  # Total number of elements in both arrays
    half = (total + 1) // 2  # Half of the total elements (for partitioning)

    low, high = 0, n1  # Initialize binary search bounds

    # Perform binary search to find the correct partition
    while low <= high:
        mid1 = (low + high) // 2  # Partition index in nums1
        mid2 = half - mid1  # Partition index in nums2

        # Edges: use -inf / +inf when partition is at array boundaries
        left1 = (
            nums1[mid1 - 1] if mid1 > 0 else -float("inf")
        )  # Left max of nums1
        right1 = (
            nums1[mid1] if mid1 < n1 else float("inf")
        )  # Right min of nums1
        left2 = (
            nums2[mid2 - 1] if mid2 > 0 else -float("inf")
        )  # Left max of nums2
        right2 = (
            nums2[mid2] if mid2 < n2 else float("inf")
        )  # Right min of nums2

        # Found correct partition when left parts ≤ right parts
        if left1 <= right2 and left2 <= right1:
            # Odd total length: median is max of left sides
            if total % 2:
                return max(left1, left2)  # Return the max of the left parts
            # Even total length: average of max(lefts) and min(rights)
            return (
                max(left1, left2) + min(right1, right2)
            ) / 2.0  # Calculate median

        # If left1 is too big, decrease mid1 to move left
        if left1 > right2:
            high = mid1 - 1  # Move the high pointer left
        else:
            # If left2 is too big, increase mid1 to move right
            low = mid1 + 1  # Move the low pointer right

'''
Time Complexity: O(log(min(n1,n2))), where n1 and n2 are the sizes of two given arrays.
Reason: We are applying binary search on the range [0, min(n1, n2)].

Space Complexity: O(1) as no extra space is used.
'''