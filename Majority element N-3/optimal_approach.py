'''
Approach Using Extended Moore's Voting Algorithm:
The steps are as follows:

-> Initialize two candidate variables (candidate1, candidate2) and their respective counters (count1, count2) as 0.
-> First Pass (Find potential candidates):
-> Traverse the array:
If count1 is 0 and the current element is not equal to candidate2, assign the current element to candidate1 and set count1 = 1.
Else if count2 is 0 and the current element is not equal to candidate1, assign the current element to candidate2 and set count2 = 1.
Else if the current element equals candidate1, increment count1.
Else if the current element equals candidate2, increment count2.
Otherwise, decrement both count1 and count2.
-> Second Pass (Verify the candidates):
Reset count1 and count2 to 0.
Traverse the array again and count the actual occurrences of candidate1 and candidate2.
-> Final Result:
If count1 > n / 3, add candidate1 to the result.
If count2 > n / 3, add candidate2 to the result.
'''
def majorityElement(nums):
    n = len(nums)
    candidate1 = 0
    candidate2 = 0
    count1 = 0
    count2 = 0

    # Phase 1: Find up to two potential candidates
    for i in range(n):
        if count1 == 0 and nums[i] != candidate2:
            candidate1 = nums[i]
            count1 = 1
        elif count2 == 0 and nums[i] != candidate1:
            candidate2 = nums[i]
            count2 = 1
        elif nums[i] == candidate1:
            count1 += 1
        elif nums[i] == candidate2:
            count2 += 1
        else:
            count1 -= 1
            count2 -= 1

    # Phase 2: Verify the candidates
    count1 = count2 = 0
    for i in range(n):
        if nums[i] == candidate1:
            count1 += 1
        elif nums[i] == candidate2:
            count2 += 1

    result = []
    if count1 > n // 3:
        result.append(candidate1)
    if count2 > n // 3:
        result.append(candidate2)

    return result
nums = [3,2,3]
ans = majorityElement(nums)

'''
Time Complexity: O(N) + O(N), where N = size of the given array.
Reason: The first O(N) is to calculate the count and find the expected majority element. The second one is to check if the expected element is the majority one or not.

Note: If the question states that the array must contain a majority element, in that case, we do not need the second check. Then the time complexity will boil down to O(N).

Space Complexity: O(1) as we are not using any extra space.
'''
