# Brute Force Approach

def nearlySorted(arr, k):
    arr.sort()
    return arr

arr = [6, 5, 3, 2, 8, 10, 9]
ans = nearlySorted(arr, 3)

'''
Time complexity: O(n*log n) 
Space complexity: O(1)
'''

# Optimal Approach
import heapq

def nearlySorted(nums, k):
    n = len(nums)
    # List to store answer
    ans = []
    # Declare empty list
    minHeap = []
    # using heapify to convert list into heap
    heapq.heapify(minHeap)
    for r in range(len(nums)):
        # adds an element into an existing heap
        heapq.heappush(minHeap, nums[r])
        if len(minHeap) > k:
            # removes the smallest element from the min heap
            ans.append(heapq.heappop(minHeap))
    # pop all remaining elements from the min-heap and store in the answer list
    while minHeap:
        ans.append(heapq.heappop(minHeap))
    # return answer
    return ans

arr = [6, 5, 3, 2, 8, 10, 9]
ans = nearlySorted(arr, 3)

'''
Time complexity: O(n*log k)
Space complexity: O(k) for Heap + O(n) for ans array
'''

def nearlySorted(nums, k):
    minHeap = []
    n = len(nums)
    # Initialize the heap with the first k elements
    for i in range(k):
        heapq.heappush(minHeap, nums[i])
    target = 0
    # Process the remaining elements
    for i in range(k, n):
        heapq.heappush(minHeap, nums[i])
        # Extract the smallest from heap and assign to the target position
        nums[target] = heapq.heappop(minHeap)
        target += 1
    # Extract remaining elements from the heap
    while minHeap:
        nums[target] = heapq.heappop(minHeap)
        target += 1
    return nums

arr = [6, 5, 3, 2, 8, 10, 9]
ans = nearlySorted(arr, 3)

'''
Time complexity: O(n*log k)
Space complexity: O(k) for Heap
'''