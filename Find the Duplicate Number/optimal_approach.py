'''
Intuition: We can solve this using the same approach as we use in cycle detection in a linked list.
'''
def findDuplicate(nums):
    # Initialize slow and fast pointers to the first element
    slow = nums[0]
    fast = nums[0]
    # Phase 1: Detect the cycle
    # Move slow by 1 step and fast by 2 steps until they meet
    while True:
        slow = nums[slow]  # Move slow pointer by one step
        fast = nums[nums[fast]]  # Move fast pointer by two steps
        if slow == fast:
            break  # Cycle detected
    # Phase 2: Find the entrance to the cycle (the duplicate number)
    # Move the fast pointer to the start of the array
    fast = nums[0]
    while slow != fast:
        slow = nums[slow]  # Move slow pointer by one step
        fast = nums[fast]  # Move fast pointer by one step
    # Both pointers now meet at the entrance of the cycle, which is the duplicate number
    return slow  # Return the duplicate number (We can return fast also as both slow and fast are at same position)

nums = [1,3,4,2,2]
ans = findDuplicate(nums)

'''
Time complexity: O(N). Since we traversed through the array only once.

Space complexity: O(1).
'''