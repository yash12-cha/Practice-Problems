# Brute Force Approach

def kDistinctChars(k, s):
    ans = -1
    n = len(s)
    for i in range(n):
        freq = {}
        distinct = 0
        for j in range(i, n):
            if s[j] not in freq or freq[s[j]] == 0:
                freq[s[j]] = 1
                distinct += 1
            else:
                freq[s[j]] += 1
            if distinct == k:
                ans = max(ans, j-i+1)
            if distinct > k:
                break
    return ans

s = "aababbcaacc"
k = 2
ans = kDistinctChars(k, s)

'''
🎯 Complexity (Brute-Force)
Time: O(n²) — two nested loops over n and O(1) operations inside.

Space: O(n) — in the worst case, freq can grow to store up to n unique elements.
'''

# Optimal Approach
def kDistinctChars(k, s):
    count = {}
    left = 0
    max_length = 0
    distinct = 0
    
    for right in range(len(s)):
        right_char = s[right]
        count[right_char] = count.get(right_char,0) + 1
        if count[right_char] == 1:
            distinct += 1
        
        while distinct > k:
            left_char = s[left]
            count[left_char] -= 1
            if count[left_char] == 0:
                distinct -= 1
            left += 1
        
        max_length = max(max_length, right-left+1)
    
    return max_length

s = "aababbcaacc"
k = 2
ans = kDistinctChars(k, s)

'''
Time Complexity: 
O(n), where n is the length of the string s. Each character is processed at most twice (once by the right pointer and once by the left pointer).

Space Complexity: 
O(k) for the dictionary that stores the count of distinct characters.
'''