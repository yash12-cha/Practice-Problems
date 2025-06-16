# Brute Force Approach

def topKFrequent(nums, k):
    # Step 1: Count the frequency of each element in nums
    freq_map = {}
    for ele in nums:
        freq_map[ele] = freq_map.get(ele, 0) + 1  # Increment the count for each element
    # Step 2: Create a list of (element, frequency) tuples
    items_list = []
    for ele in freq_map:
        count = freq_map[ele]
        items_list.append((ele, count))  # Append the element and its frequency as a tuple
    # Step 3: Define a function to extract frequency for sorting
    def get_frequency(item):
        return item[1]  # Return the frequency part of the tuple
    # Step 4: Sort the list of tuples by frequency in descending order
    freq_list = sorted(items_list, key=get_frequency, reverse=True)
    # Step 5: Extract the top k frequent elements
    res = []
    for i in range(k):
        res.append(freq_list[i][0])  # Append only the element (not the frequency)
    return res  # Return the list of top k frequent elements

nums = [1,1,1,2,2,3]
k = 2
ans = topKFrequent(nums, k)

'''
Time Complexity:

- Iterates through nums: O(n)
- Iterates over u unique elements: O(u) (Build list of tuples)
- Sorting u items: O(u log u) (Sort the list by frequency)
- Extracting k items: O(k)
- Overall: O(n log n)

Space Complexity:

- freq_map → O(u)
- items_list and freq_list → O(u)
- res (final output) → O(k)
- Overall: O(u+k)
'''

# Optimal Approach

import heapq

def topKFrequent(nums, k):
    # Step 1: Count the frequency of each element and store it in a hashmap
    freq = {}
    for i in nums:
        if i in freq:
            freq[i] += 1  # Increment the count if the element is already in the hashmap
        else:
            freq[i] = 1  # Initialize the count to 1 if the element is not in the hashmap

    # Step 2: Declare an empty list to use as a min-heap
    minHeap = []
    # Using heapify to convert the list into a heap (not necessary here since it's empty)

    # Step 3: Iterate over the frequency map
    for i in freq:
        # Insert the (frequency, element) pair into the min-heap
        heapq.heappush(minHeap, (freq[i], i))
        
        # If the size of the heap exceeds k, remove the smallest element
        if len(minHeap) > k:
            heapq.heappop(minHeap)  # This ensures we keep only the top k frequent elements

    # Step 4: Extract the elements from the min-heap into the result list
    res = []
    for fre, val in minHeap:
        res.append(val)  # Append only the element (not the frequency)

    # Step 5: Sort the result list before returning (optional, based on requirements)
    res.sort()  # Sort the result list to maintain a consistent order

    return res  # Return the list of top k frequent elements

# Example usage
nums = [1, 1, 1, 2, 2, 3]
k = 2
ans = topKFrequent(nums, k)


'''
Time Complexity:

- Iterates through nums: O(n)
- For u unique elements, each push/pop is O(log k), Total → O(u log k)
- Build result list: O(k)
- Sort the result list: O(k log k)
- Overall: O(n log k + k log k)

Space Complexity:

- freq_map → O(u)
- Min-heap → At most k elements → O(k
- Result list res → O(k)
- Overall: O(u+k)
'''