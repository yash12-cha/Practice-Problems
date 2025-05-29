'''
Intuition: For each number between 1 to N, we will try to count the occurrence in the given array using linear search. And the element with occurrence as 2 will be the repeating number and the number with 0 occurrences will be the missing number.
'''

def findTwoElement(arr):
    repeating = -1
    missing = -1
    for i in range(1, len(arr) + 1):
        count = 0  # Reset count for each number i
        for j in range(len(arr)):
            if arr[j] == i:
                count += 1
        if count == 2:
            repeating = i
        if count == 0:
            missing = i
        # Break if both repeating and missing are found
        if repeating != -1 and missing != -1:
            break
    return [repeating, missing]

nums = [4, 3, 6, 2, 1, 1]
ans = findTwoElement(nums)

'''
Time Complexity: O(N2), where N = size of the given array.
Reason: Here, we are using nested loops to count occurrences of every element between 1 to N.

Space Complexity: O(1) as we are not using any extra space.
'''