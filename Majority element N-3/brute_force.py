'''
Approach:
The steps are as follows:

We will run a loop that will select the elements of the array one by one.
Now, for each unique element, we will run another loop and count its occurrence in the given array.
If any element occurs more than the floor of (N/3), we will include it in our answer. 
While traversing if we find any element that is already included in our answer, we will just skip it.
'''

def majorityElement(nums):
    n = len(nums)
    result = []

    # Check frequency of each element
    for i in range(n):
        count = 0
        for j in range(n):
            if nums[i] == nums[j]:
                count += 1

        # Add to result if count > n // 3 and not already added
        if count > n // 3 and nums[i] not in result:
            result.append(nums[i])

    return result

nums = [3,2,3]
ans = majorityElement(nums)

'''
Time Complexity: O(N^2), where N = size of the given array.
Reason: For every element of the array the inner loop runs for N times. And there are N elements in the array. So, the total time complexity is O(N^2).

Space Complexity: O(1) as we are using a list that stores a maximum of 2 elements. The space used is so small that it can be considered constant.
'''