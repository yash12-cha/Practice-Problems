# Brute Force Approach

def minCost(arr):
    total_cost = 0  # Initialize total cost to zero
    
    # Loop until only one rope remains in the array
    while len(arr) > 1:
        arr.sort()  # Sort the ropes in ascending order to get the two smallest ropes
        
        # Remove the two smallest ropes
        first = arr.pop(0)
        second = arr.pop(0)
        
        cost = first + second  # Cost to connect these two ropes is the sum of their lengths
        total_cost += cost     # Accumulate the cost
        
        arr.append(cost)  # Add the combined rope back to the array
    
    return total_cost  # Return the total minimum cost to connect all ropes

arr = [4, 3, 2, 6]
ans = minCost(arr)

'''
Time Complexity: O(n^2*log(n)), the sorting operation is performed n-1 times, and the size of the array decreases with each iteration

Space Complexity: O(1)
'''

# Optimal Approach

import heapq
def minCost(arr):
    # Initialize a min heap with all rope lengths
    minHeap = []
    heapq.heapify(minHeap)
    # Push all elements from the array into the min heap
    for ele in arr:
        heapq.heappush(minHeap, ele)
    res = 0  # Initialize total cost
    
    # Continue until there is only one rope left
    while len(minHeap) > 1:
        # Pop the two smallest rope lengths
        first = heapq.heappop(minHeap)
        second = heapq.heappop(minHeap)
        cost = first + second  # Cost to connect these two ropes
        res += cost            # Add cost to total
        
        # Push the combined rope length back into the min heap
        heapq.heappush(minHeap, cost)
    return res  # Return the total minimum cost to connect all ropes

arr = [4, 3, 2, 6]
ans = minCost(arr)

'''
Time Complexity: O(n logn) because each insertion and extraction from the heap takes O(logn), repeated for all ropes.

Space Complexity: O(n) to store all the ropes initially in the heap.
'''