# Brute Force approach

def subarraysWithKDistinct(nums, k):
    ans = 0
    n = len(nums)

    for i in range(n):
        freq = {}       # counts of elements in the current subarray
        distinct = 0    # number of distinct elements so far
        
        # Check all subarrays starting at i
        for j in range(i, n):
            if nums[j] not in freq or freq[nums[j]] == 0:
                freq[nums[j]] = 1
                distinct += 1
            else:
                freq[nums[j]] += 1
            
            # If we reached exactly k distinct elements, this subarray is valid
            if distinct == k:
                ans += 1
            # Once distinct > k, no need to extend further from this start
            if distinct > k:
                break

    return ans

nums = [1,2,1,2,3]
k = 2
ans = subarraysWithKDistinct(nums, k)

'''
🎯 Complexity (Brute-Force)
Time: O(n²) — two nested loops over n and O(1) operations inside.

Space: O(n) — in the worst case, freq can grow to store up to n unique elements.
'''

# Optimal approach
def atMostK(nums, k):
    count = {}
    left = 0
    total = 0
    distinct = 0
    
    for right in range(len(nums)):
        right_char = nums[right]
        count[right_char] = count.get(right_char,0) + 1
        if count[right_char] == 1:
            distinct += 1
        
        while distinct > k:
            left_char = nums[left]
            count[left_char] -= 1
            if count[left_char] == 0:
                distinct -= 1
            left += 1
        
        total += right - left + 1
    
    return total
def subarraysWithKDistinct(nums, k):
    return atMostK(nums, k) - atMostK(nums, k-1)

nums = [1,2,1,2,3]
k = 2
ans = subarraysWithKDistinct(nums, k)

'''
⏱ Time Complexity:
Each element is processed at most twice: once by the right pointer, and once by the left pointer during shrinking.

So the total time is O(n), where n = len(nums).

💾 Space Complexity:
O(n) The space complexity depends on the dictionary count that stores the frequency of characters currently within the window.
'''