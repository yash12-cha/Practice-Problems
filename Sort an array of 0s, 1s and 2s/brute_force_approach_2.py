def sort012(nums):
    nums.sort()
    return nums


# Example usage
nums = [2, 0, 2, 1, 1, 0]
ans = sort012(nums)

'''
Time and Space Complexity:
-> Time Complexity: O(n log n), where n is the length of the input array.
-> Space Complexity: O(1) for in-place sorting, but O(n) if considering the space used by the sort function's internal operations.
'''
