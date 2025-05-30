'''
Intuition: Take a frequency array of size N+1 and initialize it to 0. Now traverse through the array and if the frequency of the element is 0 increase it by 1, else if the frequency is not 0 then that element is the required answer.
'''
def findDuplicate(nums):
    n = len(nums)
    freq = [0] * (n+1)
    for i in range(n):
        if freq[nums[i]] == 0:
            freq[nums[i]] += 1
        else:
            return nums[i]
        
nums = [1,3,4,2,2]
ans  = findDuplicate(nums)

'''
Time Complexity: O(N), as we are traversing through the array only once.

Space Complexity: O(N), as we are using extra space for frequency array.
'''