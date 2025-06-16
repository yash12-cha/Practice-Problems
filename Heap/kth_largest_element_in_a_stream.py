from typing import List

# Brute Force Approach

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.data = nums[:]  # Create a copy of nums
        self.data.sort(reverse=True)  # Sort in descending order
        self.len_nums = len(self.data)

        

    def add(self, val: int) -> int:
        # If the length exceeds k, remove the smallest element
        if self.len_nums > self.k:
            self.data.pop()  # Remove the smallest element (last in sorted order)
            self.len_nums -= 1
        
        # Add the new value to the list
        self.data.append(val)
        self.len_nums += 1
        
        # Sort the list after adding the new value
        self.data.sort(reverse=True)
        
        # Return the k-th largest element
        return self.data[self.k - 1]  # k-th largest is at index k-1
    
# Example Usage
kth = KthLargest(3, [4, 5, 8, 2])
print(kth.add(3))  # Output: 4
print(kth.add(5))  # Output: 5
print(kth.add(10)) # Output: 5
print(kth.add(9))  # Output: 8
print(kth.add(4))  # Output: 8

'''
Time Complexity:

- Sorting takes O(n log n) where n = len(nums)
- self.data.pop() – O(1)
- self.data.append(val) – O(1)
- self.data.sort(reverse=True) – O(m log m), where m = len(self.data) (at most k + 1)
- Indexing self.data[k - 1] – O(1)
👉 Since you only keep at most k + 1 elements:
    - Sorting is O(k log k)

Space Complexity:

- You store at most k + 1 elements in self.data → O(k)
'''

# Optimal Approach

import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = []
        
        # Add each number in nums to the min heap
        for ele in nums:
            heapq.heappush(self.minHeap, ele)
            # Maintain size at most k
            if len(self.minHeap) > k:
                heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        # Push the new value
        heapq.heappush(self.minHeap, val)
        # If heap size exceeds k, remove smallest
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        # The root of the min heap is the k-th largest
        return self.minHeap[0]
    
# Example Usage
kth = KthLargest(3, [4, 5, 8, 2])
print(kth.add(3))  # Output: 4
print(kth.add(5))  # Output: 5
print(kth.add(10)) # Output: 5
print(kth.add(9))  # Output: 8
print(kth.add(4))  # Output: 8

'''
Time Complexity:

- Each push/pop is O(log k) -> Total time = O(n log k)
- add() method -> Always O(log k)

Space Complexity:

- Heap stores at most k elements → O(k)
'''