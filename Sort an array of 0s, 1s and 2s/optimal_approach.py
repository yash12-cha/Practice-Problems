'''
Dutch National Flag Algorithm

The Dutch National Flag algorithm is used to sort an array containing three distinct values (in this case, 0s, 1s, and 2s) in a single pass. The goal is to partition the array into three parts:

arr[0] to arr[low - 1]: This part will contain all the zeros.
arr[low] to arr[mid - 1]: This part will contain all the ones.
arr[high + 1] to arr[n - 1]: This part will contain all the twos, where is the length of the array.

The steps will be the following:

-> First, we will run a loop that will continue until mid <= high.

-> There can be three different values of mid pointer i.e. arr[mid]
- If arr[mid] == 0, we will swap arr[low] and arr[mid] and will increment both low and mid. Now the subarray from index 0 to (low-1) only contains 0.
- If arr[mid] == 1, we will just increment the mid pointer and then the index (mid-1) will point to 1 as it should according to the rules.
- If arr[mid] == 2, we will swap arr[mid] and arr[high] and will decrement high. Now the subarray from index high+1 to (n-1) only contains 2. In this step, we will do nothing to the mid-pointer as even after swapping, the subarray from mid to high(after decrementing high) might be unsorted. So, we will check the value of mid again in the next iteration.

-> Finally, our array should be sorted.
'''

def sort012(nums):
    low, mid, high = 0, 0, len(nums) - 1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
    return nums

# Example usage
nums = [2, 0, 2, 1, 1, 0]
ans = sort012(nums)

'''
Time and Space Complexity:
-> Time Complexity O(n): The algorithm performs a single pass through the array, examining each element exactly once. This linear time complexity makes it highly efficient for sorting arrays with three distinct elements.
-> Space Complexity O(1): The algorithm sorts the array in place, requiring only a constant amount of additional memory for pointer variables (low, mid, and high). No extra space proportional to the input size is needed.
'''