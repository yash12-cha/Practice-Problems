'''
Intuition: Instead of counting the occurrences every time, using the hashing technique, we will store the frequency of each element between 1 to N. Now, the element with frequency 2 will be the repeating number and the element with frequency 0 will be the missing number.
'''
def findTwoElement(arr):
    hash_map = {}
    repeating = -1
    missing = -1
    # Count occurrences of each element
    for ele in arr:
        if ele in hash_map:
            hash_map[ele] += 1
        else:
            hash_map[ele] = 1
    # Check for repeating and missing elements
    for ele in range(1, len(arr) + 1):
        if ele in hash_map and hash_map[ele] == 2:
            repeating = ele
        if ele not in hash_map:
            missing = ele
        # Break if both repeating and missing are found
        if repeating != -1 and missing != -1:
            break
    return [repeating, missing]

nums = [4, 3, 6, 2, 1, 1]
ans = findTwoElement(nums)

'''
Time Complexity: O(2N), where N = the size of the given array.
Reason: We are using two loops each running for N times. So, the time complexity will be O(2N).

Space Complexity: O(N) as we are using a hash array to solve this problem.
'''