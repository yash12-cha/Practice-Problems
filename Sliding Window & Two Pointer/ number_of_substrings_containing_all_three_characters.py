# Brute Force Approach
def numberOfSubstrings(s):
    cnt = 0
    for i in range(len(s)):
        a_c = 0
        b_c = 0
        c_c = 0
        for j in range(i, len(s)):
            if s[j] == "a":
                a_c += 1
            elif s[j] == "b":
                b_c += 1
            else:
                c_c += 1
            if a_c > 0 and b_c > 0 and c_c > 0:
                cnt += 1
    return cnt

s = "abcabc"
ans = numberOfSubstrings(s)

'''
🧠 Time and Space Complexity:
Time: O(n²) — nested loops for each starting index.

Space: O(1)
'''

# Optimal Approach
def numberOfSubstrings(s):
    # Two-pointer sliding window: [left, right]
    left = 0
    count = {}  # counts of characters in current window
    total_substrings = 0
    
    # Expand the window by moving right
    for right in range(len(s)):
        c = s[right]
        count[c] = count.get(c, 0) + 1
        
        # Once the window has at least one 'a', 'b', and 'c', 
        # every substring starting anywhere from left to right and ending at or beyond right is valid.
        while len(count) == 3:
            # substrings starting at left and ending anywhere from right to end:
            total_substrings += len(s) - right
            
            # shrink window from the left
            left_char = s[left]
            count[left_char] -= 1
            if count[left_char] == 0:
                del count[left_char]
            left += 1
    
    return total_substrings

s = "abcabc"
ans = numberOfSubstrings(s)

'''
🧠 Complexity Analysis
Time Complexity: O(n), where n = len(s). Both pointers move forward only, so each character is processed a constant number of times 

Space Complexity: O(1). The count dictionary only ever holds up to three keys: 'a', 'b', 'c' 
'''