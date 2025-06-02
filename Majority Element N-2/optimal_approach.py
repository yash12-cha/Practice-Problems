'''
Approach Using Moore's Voting Algorithm:
The steps are as follows:

Initialize a candidate variable and a count variable.
Traverse the array once:
-> If countis zero, set the candidate to the current element and set count to one.
-> If the current element equals the candidate, increment count.
-> If the current element differs from the candidate, decrement count.
-> Traverse the array again to count the occurrences of the candidate.
-> If the candidate's count is greater than n / 2, return the candidate as the majority element.
'''
def majorityElement(nums):
    n = len(nums)
    candidate = 0
    count = 0

    # Phase 1: Find a potential majority element
    for i in range(n):
        if count == 0:
            candidate = nums[i]
            count = 1
        elif nums[i] == candidate:
            count += 1
        else:
            count -= 1

    # Phase 2: Verify the candidate
    actual_count = 0
    for i in range(n):
        if nums[i] == candidate:
            actual_count += 1

    if actual_count > n // 2:
        return candidate
    return -1

nums = [3,2,3]
ans = majorityElement(nums)
print(ans)

'''
Time Complexity: O(N) + O(N), where N = size of the given array.
Reason: The first O(N) is to calculate the count and find the expected majority element. The second one is to check if the expected element is the majority one or not.

Note: If the question states that the array must contain a majority element, in that case, we do not need the second check. Then the time complexity will boil down to O(N).

Space Complexity: O(1) as we are not using any extra space.
'''
