'''
Intuition: Sort the array. After that, if there is any duplicate number they will be adjacent.So we simply have to check if arr[i]==arr[i+1] and if it is true,arr[i] is the duplicate number.
'''

def findDuplicate(nums):
    nums.sort()
    repeated  = -1
    for i in range(len(nums)):
        if nums[i] == nums[i+1]:
            repeated = nums[i]
            break
    return repeated

nums = [1,3,4,2,2]
ans  = findDuplicate(nums)

'''
Time Complexity:O(Nlogn + N)

Reason: NlogN for sorting the array and O(N) for traversing through the array and checking if adjacent elements are equal or not. But this will distort the array.

Space Complexity: O(1) as we are not using any extra space.
'''