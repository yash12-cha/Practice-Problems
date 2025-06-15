# Brute Force Approach 

def findKthLargest(nums, k):
    
    nums.sort()  # Sort the list in ascending order
    # Return the element at index -k (k-th largest)
    return nums[-k]

nums = [3,2,1,5,6,4]
k = 2
ans = findKthLargest(nums, k)

'''
Time complexity: O(nlogn)

Space complexity: O(1)
'''

# Optimal Approach

import heapq

def findKthLargest(nums,k):
    # Declare empty list
    minHeap = []
    # using heapify to convert list into heap
    heapq.heapify(minHeap)
    for r in range(len(nums)):
        # adds an element into an existing heap
        heapq.heappush(minHeap, nums[r])
        if len(minHeap) > k:
            # removes the smallest element from the min heap
            heapq.heappop(minHeap)
    # removes and returns the smallest element from the min heap
    return heapq.heappop(minHeap)

nums = [3,2,1,5,6,4]
k = 2
ans = findKthLargest(nums, k)

'''
Time complexity: O(k+(n-k)*log(k))  , n = size of array

Space complexity: O(k)
'''

def partition(arr, left, right):
    
    pivot = arr[left]  # Choose the leftmost element as the pivot
    l = left + 1  # Start the left pointer just after the pivot
    r = right  # Start the right pointer at the end of the array
    
    # Continue until the left pointer exceeds the right pointer
    while l <= r:
        # Move the left pointer to the right while the current element is less than the pivot
        if arr[l] < pivot and arr[r] > pivot:
            # If both pointers are in the correct position, swap the elements
            arr[l], arr[r] = arr[r], arr[l]
            l += 1  # Move the left pointer to the right
            r -= 1  # Move the right pointer to the left
        
        # If the left pointer points to an element greater than or equal to the pivot, move it right
        if arr[l] >= pivot:
            l += 1
        
        # If the right pointer points to an element less than or equal to the pivot, move it left
        if arr[r] <= pivot:
            r -= 1
            
    # Place the pivot in its correct position by swapping it with the right pointer
    arr[left], arr[r] = arr[r], arr[left]
    
    # Return the final index of the pivot, which is now in its correct sorted position
    return r


def findKthLargest(arr, k):
    
    left = 0  # Starting index of the array
    right = len(arr) - 1  # Ending index of the array
    
    while True:
        # Partition the array and get the index of the pivot
        idx = partition(arr, left, right)
        
        # Check if the pivot index is the k-th largest position
        if idx == k-1:  # Adjust for 0-based index
            return arr[idx]  # Return the k-th largest element
        elif idx < k-1:
            left = idx + 1  # Search in the right subarray
        else:
            right = idx - 1  # Search in the left subarray


nums = [3,2,1,5,6,4]
k = 2
ans = findKthLargest(nums, k)

'''
Time complexity: O(n) ,where n = size of the array

Space complexity: O(1)
'''