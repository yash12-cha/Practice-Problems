def sort012(nums):
    red, white, blue = 0, 0, 0

    # Count the occurrences of 0s, 1s, and 2s
    for num in nums:
        if num == 0:
            red += 1
        elif num == 1:
            white += 1
        else:
            blue += 1
    # Create the sorted output list
    ans = [0] * red + [1] * white + [2] * blue
    return ans


# Example usage
nums = [2, 0, 2, 1, 1, 0]
ans = sort012(nums)

'''
Time and Space Complexity:
-> Time Complexity: O(n), where n is the length of the input array.
-> Space Complexity: O(n), due to the creation of a new list to store the sorted elements.
'''
