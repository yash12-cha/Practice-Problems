# Brute Force Approach

def characterReplacement(s,k):
    max_len = 0  # To store the maximum length of the substring found
    # Iterate over each starting index of the substring
    for i in range(len(s)):
        char_cnt = {}  # Dictionary to count characters in the current window
        max_freq = 0   # To track the maximum frequency of any character in the current window
        
        # Iterate over each ending index of the substring
        for j in range(i, len(s)):
            # Increment the count of the current character
            if s[j] in char_cnt:
                char_cnt[s[j]] += 1
            else:
                char_cnt[s[j]] = 1
            
            # Update the maximum frequency of any character in the current window
            max_freq = max(max_freq, char_cnt[s[j]])
            
            # Calculate the length of the current window
            window_len = j - i + 1
            
            # Calculate the number of changes needed
            changes = window_len - max_freq
            
            # If the number of changes is within the allowed limit, update max_len
            if changes <= k:
                max_len = max(max_len, window_len)
    return max_len

s = "ABAB"
k = 2
ans = characterReplacement(s, k)

'''
🧠 Time and Space Complexity:
Time: O(n²) — nested loops for each starting index.

Space: O(26)
'''

# Optimal Approach
def characterReplacement(s, k):
    left = 0
    max_len = 0
    char_cnt = {}  # Dictionary to count characters in the current window
    max_freq = 0   # Frequency of the most common character in the window

    for right in range(len(s)):
        # Add current character to the count dictionary
        char_cnt[s[right]] = char_cnt.get(s[right], 0) + 1

        # Update max_freq if needed
        max_freq = max(max_freq, char_cnt[s[right]])

        # Total characters in window: right - left + 1
        # If we need to change more than k characters, shrink the window
        if (right - left + 1) - max_freq > k:
            char_cnt[s[left]] -= 1  # Remove the character going out of window
            left += 1               # Shrink window from the left

        # Update max_len to track the longest valid window seen so far
        max_len = max(max_len, right - left + 1)

    return max_len

s = "AABABBA"
k = 1
ans = characterReplacement(s, k)

'''
Time Complexity: O(n)
Space Complexity: O(26)
'''