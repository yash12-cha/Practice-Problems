def sort012(nums):
    red, white, blue = 0, 0, 0
    for num in nums:
        if num == 0:
            red += 1
        elif num == 1:
            white += 1
        else:
            blue += 1
    index = 0
    for _ in range(red):
        nums[index] = 0
        index += 1
    for _ in range(white):
        nums[index] = 1
        index += 1
    for _ in range(blue):
        nums[index] = 2
        index += 1
    return nums

# Example usage
nums = [2, 0, 2, 1, 1, 0]
ans = sort012(nums)


'''
Time Complexity: O(n) + O(n)
-> The algorithm traverses the array twice: once to count the number of 0s, 1s, and 2s, and a second time to overwrite the original array with the sorted values.
-> Each traversal processes each element exactly once, leading to a linear time complexity relative to the size of the array.

Space Complexity: O(1)
-> The algorithm uses a constant amount of additional space: three integer variables to count the occurrences of 0s, 1s, and 2s, and a few pointers for indexing.
-> No additional data structures or arrays are utilized, ensuring constant auxiliary space usage.
'''