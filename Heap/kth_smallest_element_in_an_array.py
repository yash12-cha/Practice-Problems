# Brute Force Approach 

def findKthSmallest(nums, k):
    
    nums.sort()  # Sort the list in ascending order
    # Return the element at index k - 1 (k-th largest)
    return nums[k-1]

nums = [7, 10, 4, 3, 20, 15]
k = 3
ans = findKthSmallest(nums, k)

'''
Time complexity: O(nlogn)

Space complexity: O(1)
'''

# Optimal Approach

import heapq

def findKthSmallest(nums,k):
    n = len(nums)
    # Declare empty list
    maxHeap = []
    # using heapify to convert list into heap
    heapq.heapify(maxHeap)
    for r in range(n):
        # Adding items to the heap using heappush
        # function by multiplying them with -1
        heapq.heappush(maxHeap, -1 * nums[r])
        if len(maxHeap) > k:
            # removes the smallest element from the max heap
            heapq.heappop(maxHeap)
    # removes and returns the smallest element from the max heap
    c = heapq.heappop(maxHeap)
    # multiplying with -1
    return -1 * c

nums = [7, 10, 4, 3, 20, 15]
k = 3
ans = findKthSmallest(nums, k)

'''
Time complexity: O(k+(n-k)*log(k))  , n = size of array

Space complexity: O(k)
'''

def partition(arr, left, right):
    pivot = arr[left]
    l = left + 1
    r = right

    while l <= r:
        if arr[l] > pivot and arr[r] < pivot:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1

        if arr[l] <= pivot:
            l += 1
        if arr[r] >= pivot:
            r -= 1

    arr[left], arr[r] = arr[r], arr[left]
    return r

def kthSmallest(arr,k):
    left = 0
    right = len(arr) - 1

    while True:
        idx = partition(arr, left, right)
        
        if idx == k - 1:
            return arr[idx]
        elif idx < k - 1:
            left = idx + 1
        else:
            right = idx - 1

nums = [7, 10, 4, 3, 20, 15]
k = 3
ans = findKthSmallest(nums, k)


'''
Time complexity: O(n) ,where n = size of the array

Space complexity: O(1)
'''