'''
Approach:
The steps are as follows:

We will run a loop that will select the elements of the array one by one.
Now, for each element, we will run another loop and count its occurrence in the given array.
If any element occurs more than the floor of (N/2), we will simply return it.
'''

def majorityElement(nums):
    n = len(nums)
    
    for i in range(n):
        count = 0
        for j in range(n):
            if nums[i] == nums[j]:
                count += 1
        
        if count > n // 2:
            return nums[i]
    
    return -1

nums = [3,2,3]
ans = majorityElement(nums)

'''
Time Complexity: O(N^2), where N = size of the given array. Reason: For every element of the array the inner loop runs for N times. And there are N elements in the array. So, the total time complexity is O(N^2). 
Space Complexity: O(1) as we use no extra space.
'''