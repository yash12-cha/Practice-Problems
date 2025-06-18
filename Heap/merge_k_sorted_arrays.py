# Brute Force Approach

from typing import List

def mergeKSortedArrays(nums: List[List[int]]) -> List[int]:
    combined = []

    # Manually append elements from each array to combined list
    for i in range(len(nums)):
        for j in range(len(nums[i])):
            combined.append(nums[i][j])

    # Sort the combined array
    combined.sort()

    return combined

# Example usage:
nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ans = mergeKSortedArrays(nums)

'''
Time Complexity:

Appending all elements: O(n) for total number of elements n
Sorting combined array: O(nlogn)
Overall: O(nlogn)

Space Complexity:

Uses O(n) space for the combined array.
'''
# Optimal Approach

import heapq
def mergeKSortedArrays(nums, k):
    # List to store answer
    result = []
    # Declare empty list
    minHeap = []
    # using heapify to convert list into heap
    heapq.heapify(minHeap)
    for i in range(len(nums)):
        # insert the first element of all the arrays
        # along with its indices and array number
        heapq.heappush(minHeap, (nums[i][0], i, 0))
    while len(minHeap) > 0:
        # Remove the minimum element from the heap.
        curr = heapq.heappop(minHeap)
        # i is the array number
        # j is the index of the removed element in the ith array.
        i = curr[1]
        j = curr[2]
        # Add the removed element to the output array.
        result.append(curr[0])

        # If the extracted element's array has more elements, push its next one in heap
        if j + 1 < len(nums[i]):
            heapq.heappush(minHeap, (nums[i][j + 1], i, j + 1))

    # Return the output array.
    return result

nums = [[1,2,3],[4,5,6],[7,8,9]]
k = 3
ans = mergeKSortedArrays(nums, k)

'''
Time Complexity:
O(N×logk)

Space Complexity:
O(N) total (including output) or O(k) auxiliary
'''