'''
Approach:
The idea is to use a hash map to count the occurrences of each element in the array. 

Traverse the array once, and for each element, update its count in the hash map.
After updating the count, check if count exceeds n / 3.
If such an element is found, return it immediately.
If no element's count exceeds n / 3, return-1.
'''

def majorityElement(nums):
    n = len(nums)
    hash_map = {}
    ans = []

    # Count the frequency of each element
    for num in nums:
        if num in hash_map:
            hash_map[num] += 1
        else:
            hash_map[num] = 1

    # Check if any element appears more than n // 3 times
    for key, value in hash_map.items():
        if value > n // 3:
            ans.append(key)

    return ans

nums = [3,2,3]
ans = majorityElement(nums)

'''
⏱️ Time Complexity: O(n)
First loop (frequency count): O(n)

Second loop (checking majority): O(n) in the worst case
→ Total: O(n + n) = O(n)

📦 Space Complexity: O(n)
In the worst case (all elements are unique), the hash map stores n keys → O(n) space.
'''