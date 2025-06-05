# (even, odd) --> Left Half
# (odd, even) ---> Right Half

# Brute Force Approach 1
def singleNonDuplicate(nums):
    freq = {}
    for i in nums:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    for i in freq:
        if freq[i] == 1:
            return i

nums = [1,1,2,3,3,4,4,8,8]
ans = singleNonDuplicate(nums)


'''
Time and Space Complexity:

Time Complexity: O(n), where n is the number of elements in the list.

Space Complexity: O(n), as we are using hashmap to store the count
'''

# Brute Force Approach 2

def singleNonDuplicate(nums):
    n = len(nums)

    # If the list has only one element, return it.
    if n == 1:
        return nums[0]

    # Check if the first element is unique.
    if nums[0] != nums[1]:
        return nums[0]

    # Check if the last element is unique.
    if nums[n - 1] != nums[n - 2]:
        return nums[n - 1]

    # Iterate through the list, starting from the second element and ending at the second-to-last.
    for i in range(1, n - 1):
        # If the current element is not equal to its neighbors, it's the unique one.
        if nums[i] != nums[i - 1] and nums[i] != nums[i + 1]:
            return nums[i]

nums = [1,1,2,3,3,4,4,8,8]
ans = singleNonDuplicate(nums)

'''
Time and Space Complexity:

Time Complexity: O(n), where n is the number of elements in the list.

Space Complexity:  O(1), as no additional data structures are used.
'''


# Better Approach

def singleNonDuplicate(nums):
    # Initialize the result variable to 0.
    # This will hold the cumulative XOR of all elements.
    ans = 0

    # Iterate through each number in the list.
    for num in nums:
        # Apply XOR between the current result and the current number.
        # The XOR operation has the following properties:
        # 1. a ^ a = 0 (a number XORed with itself is 0)
        # 2. a ^ 0 = a (a number XORed with 0 remains unchanged)
        # 3. XOR is commutative and associative, so the order doesn't matter.
        # By XORing all numbers, pairs will cancel each other out,
        # leaving the unique number that appears only once.
        ans ^= num

    # After processing all numbers, 'ans' holds the single number.
    return ans

nums = [1,1,2,3,3,4,4,8,8]
ans = singleNonDuplicate(nums)

'''
Time and Space Complexity:

Time Complexity: O(n), where n is the number of elements in the list.

Space Complexity: O(1), as no additional data structures are used.
'''

# Optimal Approach

def singleNonDuplicate(arr):
    n = len(arr)  # Size of the array

    # Edge cases:
    if n == 1:
        return arr[0]
    if arr[0] != arr[1]:
        return arr[0]
    if arr[n - 1] != arr[n - 2]:
        return arr[n - 1]

    low = 1
    high = n - 2
    while low <= high:
        mid = (low + high) // 2

        # If arr[mid] is the single element:
        if arr[mid] != arr[mid + 1] and arr[mid] != arr[mid - 1]:
            return arr[mid]

        # We are in the left:
        if (mid % 2 == 1 and arr[mid] == arr[mid - 1]) or (mid % 2 == 0 and arr[mid] == arr[mid + 1]):
            # Eliminate the left half:
            low = mid + 1
        # We are in the right:
        else:
            # Eliminate the right half:
            high = mid - 1

    # Dummy return statement:
    return -1

nums = [1,1,2,3,3,4,4,8,8]
ans = singleNonDuplicate(nums)

'''
Time Complexity: O(logN), N = size of the given array.
Reason: We are basically using the Binary Search algorithm.

Space Complexity: O(1) as we are not using any extra space.
'''