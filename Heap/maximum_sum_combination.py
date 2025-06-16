# Brute Force Approach

def maxCombinations(K, nums1, nums2):
    # Step 1: Initialize a list to store all possible sums of elements from nums1 and nums2
    sum_ = []
    
    # Step 2: Generate all pairwise sums by adding each element of nums1 to each element of nums2
    for i in range(len(nums1)):
        for j in range(len(nums2)):
            sum_.append(nums1[i] + nums2[j])
    
    # Step 3: Sort the list of sums in descending order to prioritize the largest sums first
    sum_.sort(reverse=True)
    
    # Step 4: Extract the top K sums from the sorted list
    top_k = []
    for i in range(K):
        top_k.append(sum_[i])
    
    # Step 5: Return the list of top K sums
    return top_k

# Example usage
nums1 = [3, 2]
nums2 = [1, 4]
K = 2
ans = maxCombinations(K, nums1, nums2)

'''
Time Complexity:

- Nested Loops to Generate All Sums -> O(n * m)
- Sorting the Combined Sum List -> O(n * m * log(n * m))
- Collecting Top K Elements -> O(K)
'''

# Optimal Approach

import heapq

def maxCombinations(K, nums1, nums2):
    # Sort both arrays in descending order
    nums1.sort(reverse=True)
    nums2.sort(reverse=True)
    
    # Max heap initialization; Python heapq is min-heap, so store negative sums for max-heap behavior
    max_heap = []
    visited = set()
    
    # Initial pair: indices (0,0) and their sum (negated for max heap)
    initial_sum = nums1[0] + nums2[0]
    heapq.heappush(max_heap, (-initial_sum, 0, 0))
    visited.add((0, 0))
    
    result = []
    
    # Extract top K sums
    for _ in range(K):
        current_sum, i, j = heapq.heappop(max_heap)
        result.append(-current_sum)  # Negate back to positive sum
        
        # Next pair from nums1: (i+1, j)
        if i + 1 < len(nums1) and (i + 1, j) not in visited:
            next_sum = nums1[i + 1] + nums2[j]
            heapq.heappush(max_heap, (-next_sum, i + 1, j))
            visited.add((i + 1, j))
        
        # Next pair from nums2: (i, j+1)
        if j + 1 < len(nums2) and (i, j + 1) not in visited:
            next_sum = nums1[i] + nums2[j + 1]
            heapq.heappush(max_heap, (-next_sum, i, j + 1))
            visited.add((i, j + 1))
    
    return result

# Example usage
nums1 = [3, 2]
nums2 = [1, 4]
K = 2
ans = maxCombinations(K, nums1, nums2)

'''
Time Complexity:

- Total sorting cost: O(n log n)
- Heap operations cost: O(K log K)
- Overall: O(n log n + K log K)

Space Complexity:

- Heap space - O(K)
- Visited set - O(K)
- Result list - O(K)
'''