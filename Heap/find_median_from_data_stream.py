# Brute Force Approach 

class MedianFinder:

    def __init__(self):
        # Initialize an empty list that will be kept sorted via insertion sort logic
        self.data = []
        

    def addNum(self, num: int) -> None:
        # Insert the number in its correct sorted position using insertion sort logic
        self.data.append(num)
        i = len(self.data) - 2
        current = num

        # Shift elements greater than current to the right
        while i >= 0 and self.data[i] > current:
            self.data[i + 1] = self.data[i]
            i -= 1

        # Place current in the correct location
        self.data[i + 1] = current
        
    def findMedian(self) -> float:
        length = len(self.data)
        if length % 2 != 0:
            # Odd length: middle element is median
            return float(self.data[length // 2])
        else:
            # Even length: average two middle elements
            return (self.data[length // 2 - 1] + self.data[length // 2]) / 2.0

# Example usage
mf = MedianFinder()
mf.addNum(1)
mf.addNum(2)
print(mf.findMedian()) 
mf.addNum(3)
print(mf.findMedian())


'''
Time Complexity:

The overall time complexity is O(n^2) due to the insertion sort logic, where n is the length of the input array.

Space Complexity:

The space complexity is O(1) for the sorting operation (in-place) and O(n) for the result list.
'''
# Optimal Approach

import heapq
class MedianFinder:
    def __init__(self):
        # Initialize two heaps:
        # - left: max-heap (simulated using negative values) to store the lower half of numbers
        # - right: min-heap to store the upper half of numbers
        self.left = []  # Max-heap for the lower half
        self.right = []  # Min-heap for the upper half
    def addNum(self, num: int) -> None:
        # Add a new number to the data structure
        # Step 1: Push the number onto the max-heap (left)
        heapq.heappush(self.left, -num)  # Use negative to simulate max-heap
        
        # Step 2: Balance the heaps
        # Move the largest element from the max-heap to the min-heap
        heapq.heappush(self.right, -heapq.heappop(self.left))
        
        # Step 3: Ensure the min-heap does not have more elements than the max-heap
        if len(self.right) > len(self.left):
            # Move the smallest element from the min-heap back to the max-heap
            heapq.heappush(self.left, -heapq.heappop(self.right))
    def findMedian(self) -> float:
        # Calculate and return the median of the numbers added so far
        if len(self.left) > len(self.right):
            # If the max-heap has more elements, the median is the root of the max-heap
            return float(-self.left[0])
        # If both heaps are of equal size, the median is the average of the roots of both heaps
        return (-self.left[0] + self.right[0]) / 2.0
    

# Example usage
mf = MedianFinder()
mf.addNum(1)
mf.addNum(2)
print(mf.findMedian()) 
mf.addNum(3)
print(mf.findMedian())

'''
Time Complexity (TC):

addNum(num):
Each call to addNum involves inserting into heaps and possibly balancing them. Insertion and removal operations on a heap have a time complexity of O(log n), where n is the number of elements in the heap. Since the heaps together hold all elements, each addNum operation runs in:
O(log n)

findMedian():
This simply returns the root elements from the heaps or the average of two roots, which is an O(1) operation.

Space Complexity (SC):
The data structure maintains two heaps (left and right) that hold all the elements added so far. Thus, the total space used grows linearly with the number of elements:
O(n)
'''