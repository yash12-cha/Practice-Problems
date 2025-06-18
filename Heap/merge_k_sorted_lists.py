# Brute Force Approach

from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def convert_arr_to_linked_list(self, arr: List[int]) -> Optional[ListNode]:

        # Create a dummy node to simplify the linked list construction
        dummy_node = ListNode()
        temp = dummy_node  # Pointer to build the linked list

        # Iterate through the array and create linked list nodes
        for i in range(len(arr)):
            temp.next = ListNode(arr[i])  # Create a new node with the current array value
            temp = temp.next  # Move the pointer to the newly created node

        # Return the head of the linked list, which is the next of the dummy node
        return dummy_node.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        combined = []  # List to store values from all linked lists

        # Traverse each linked list and collect their values
        for linked_list in lists:
            current = linked_list  # Pointer to the current linked list
            while current:  # While there are nodes in the current linked list
                combined.append(current.val)  # Append the current node's value to the combined list
                current = current.next  # Move to the next node in the linked list

        # Sort the combined list of values
        combined.sort()

        # Convert the sorted array of values back into a linked list
        return self.convert_arr_to_linked_list(combined)

# Example usage:
# Creating linked lists for testing
list1 = ListNode(1, ListNode(4, ListNode(5)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
list3 = ListNode(2, ListNode(6))

lists = [list1, list2, list3]
solution = Solution()
merged_head = solution.mergeKLists(lists)

# Function to print the merged linked list
def print_linked_list(head: Optional[ListNode]):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Print the merged linked list
print_linked_list(merged_head)

'''
Time Complexity: O(K*N) + O((N*K) * log(N*K)) + O(N*K) where K is the number of linked lists and N is the length of each linked list.

O(K*N) to traverse N nodes of each of the K linked lists.
O(N*K log (N*K)) to sort the array containing all nodes ie. N nodes in K linked lists.
O(N*K) to iterate over all the sorted values in the array and convert them to the merged linked list.

Space Complexity: O(N*K) + O(N*K) where K is the number of linked lists and N is the length of each linked list.

O(N*K) to store all the N values of K linked lists into an array.
O(N*K) additional nodes that are created as part of the merged sorted linked list.
'''

# Optimal Approach

import heapq
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Merge k sorted linked lists into one sorted linked list using a min-heap.

        Args:
            lists (List[Optional[ListNode]]): List of k sorted linked lists.

        Returns:
            Optional[ListNode]: The head of the merged sorted linked list.
        """
        minHeap = []  # Initialize a min-heap to store the nodes

        # Step 1: Push the head nodes of all linked lists into the min-heap
        # Use the index of the list as a tie-breaker to avoid comparison errors
        for idx, linked_list in enumerate(lists):
            if linked_list:  # Check if the linked list is not empty
                # Push a tuple containing the node value, list index, and the node itself
                heapq.heappush(minHeap, (linked_list.val, idx, linked_list))

        # Create a dummy node to simplify the linked list construction
        dummy_node = ListNode()
        temp = dummy_node  # Pointer to build the new merged linked list

        # Step 2: While there are nodes in the min-heap
        while minHeap:
            # Pop the smallest node from the heap
            _, idx, node = heapq.heappop(minHeap)

            # Step 3: Link the current node to the merged linked list
            temp.next = node
            temp = temp.next  # Move the pointer to the newly added node

            # Step 4: If the popped node has a next node, push it into the heap
            if node.next:
                # Maintain the same list index for the next node
                heapq.heappush(minHeap, (node.next.val, idx, node.next))

        # Return the head of the merged linked list, which is next to the dummy node
        return dummy_node.next

# Example usage:
# Creating linked lists for testing
list1 = ListNode(1, ListNode(4, ListNode(5)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
list3 = ListNode(2, ListNode(6))

lists = [list1, list2, list3]
solution = Solution()
merged_head = solution.mergeKLists(lists)

# Function to print the merged linked list
def print_linked_list(head: Optional[ListNode]):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Print the merged linked list
print_linked_list(merged_head)

'''
Time Complexity: O(K log K) + O(N*K*(3*log K))where K is the number of linked lists and N is the number of nodes in each list.

O(K log K) as inserting an element into the priority queue takes log K time and is repeated K times for each list head.

Considering there are N nodes in each of the K linked lists, the overall number of nodes to be processed is N * K. For each of these N * K nodes:

Pop: Removing the smallest element (top of the priority queue) takes log K time.
Add: Adding the next element from the same list (when available) also takes log K time.
Access top: Accessing the top of the priority queue for extraction or comparison also takes log K time.
Hence, the total time complexity for the merging process across all nodes is ~ O(N * K * log K).

Space Complexity : O(K) where K is the number of linked lists. The main contributor to space usage is the priority queue which holds a node from each of these lists. Regardless of the number of nodes within each list, priority queue only holds a reference to one of its nodes at a time hence the space complexity is proportional to the number of input linked lists
'''