# Iterative Approach

def search(nums, target):
    n = len(nums)
    low = 0
    high = n - 1
    while low <= high:
        mid = (high + low) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return - 1

nums = [-1,0,3,5,9,12]
target = 9
ans = search(nums, target)

'''
Time Complexity:
In the algorithm, in every step, we are basically dividing the search space into 2 equal halves. This is actually equivalent to dividing the size of the array by 2, every time. After a certain number of divisions, the size will reduce to such an extent that we will not be able to divide that anymore and the process will stop. The number of total divisions will be equal to the time complexity.

Let’s derive the number of divisions mathematically,

If a number n can be divided by 2 for x times:
	2^x = n
Therefore, x = logn (base is 2)
So the overall time complexity is O(logN), where N = size of the given array.

Space Complexity: O(1)
'''


# Recursive Approach
def RecursiveBinarySearch(nums, low, high, target):
    # Base Condition
    if low > high:
        return - 1
    mid = (low + high) // 2
    if nums[mid] == target:
        return mid
    elif nums[mid] > target:
        return RecursiveBinarySearch(nums, low, mid-1,target)
    else:
        return RecursiveBinarySearch(nums, low+1, high,target)

def search(nums, target):
    n = len(nums)
    low = 0
    high = n - 1
    return RecursiveBinarySearch(nums, low, high, target)


nums = [-1,0,3,5,9,12]
target = 9
ans = search(nums, target)

'''
Time Complexity:
In the algorithm, in every step, we are basically dividing the search space into 2 equal halves. This is actually equivalent to dividing the size of the array by 2, every time. After a certain number of divisions, the size will reduce to such an extent that we will not be able to divide that anymore and the process will stop. The number of total divisions will be equal to the time complexity.

Let’s derive the number of divisions mathematically,

If a number n can be divided by 2 for x times:
	2^x = n
Therefore, x = logn (base is 2)
So the overall time complexity is O(logN), where N = size of the given array.

Space Complexity: O(1), If the recursive call stack is considered then the auxiliary space will be O(log N).
'''
