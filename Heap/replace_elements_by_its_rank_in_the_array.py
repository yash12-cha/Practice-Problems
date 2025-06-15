# Brute Force Approach

def replaceWithRank(arr):
    
    n = len(arr)  
    rank = [0] * n  # Initialize a list to store rank for each element
    
    # Iterate over each element to determine its rank
    for i in range(n):
        smaller = set()  # A set to keep track of unique elements smaller than arr[i]
        
        # Compare arr[i] with every other element to find smaller unique elements
        for j in range(n):
            if arr[j] < arr[i]:  
                smaller.add(arr[j])  # Add smaller element to the set
                
        # The rank is number of unique smaller elements + 1 (1-based ranking)
        rank[i] = len(smaller) + 1  
    
    return rank

arr = [20, 15, 26, 2, 98, 6]
ans = replaceWithRank(arr)

'''
Time Complexity: O(n^2) 
Space Complexity: O(N) as we are using set + O(N) for the result array
'''

# Optimal Approach

def replaceWithRank(arr):
    
    # Step 1: Extract unique elements from arr and sort them
    unique_sorted = sorted(set(arr))  # Unique sorted list
    
    # Step 2: Create a hashmap that maps each unique element to its rank
    # Ranking starts from 1 for the smallest element
    rank_map = {}
    for idx, val in enumerate(unique_sorted):
        rank_map[val] = idx + 1

    # Step 3: Replace each element in arr with its rank using the hashmap
    ranked_arr = []
    for val in arr:
        ranked_arr.append(rank_map[val])

    # Step 4: Return the new ranked array
    return ranked_arr

arr = [20, 15, 26, 2, 98, 6]
ans = replaceWithRank(arr)

'''
⏱️ Time Complexity:

Creating a set takes O(n), where n is the length of arr.
Sorting unique elements (k of them, where k ≤ n) costs O(k log k).
Building the hash map from the sorted list: O(k).
Mapping each of the n elements through the hash map: O(n).


🧠 Space Complexity:

unique_sorted: up to O(k).
rank_map: also O(k).
ranked_arr: O(n)

Total additional space (excluding input and output) is O(n + k), which simplifies to O(n)
'''

# Optimal Approach
import heapq

def replaceWithRank(N, arr):
    
    minHeap = []  # Initialize an empty min-heap
    res = [0] * N  # Result array to store ranks of elements, initialized with zeros
    heapq.heapify(minHeap)  # Heapify the empty list (optional but good practice)

    # Push all elements along with their original indices into the min-heap
    # This helps in extracting elements in ascending order while remembering their positions
    for i, val in enumerate(arr):
        heapq.heappush(minHeap, (val, i))
    
    rank = 0  # Initialize rank counter
    last = None  # Variable to keep track of the last extracted element's value (for detecting duplicates)

    # Extract elements one by one from the min-heap
    while minHeap:
        val, indx = heapq.heappop(minHeap)  # Extract the smallest element and its index
        
        # If value differs from the last extracted value, increment rank
        if last is None or last != val:
            rank += 1
        
        # Assign the current rank to the corresponding index in the result array
        res[indx] = rank
        
        last = val  # Update last extracted value
    
    return res  # Return the array of ranks

arr = [20, 15, 26, 2, 98, 6]
ans = replaceWithRank(len(arr), arr)

'''
Time Complexity: O(n * log n)
Space Complexity: O(n)
'''