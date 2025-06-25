# Brute Force Approach
def lengthOfLongestSubstring(s):
    n = len(s)
    max_len = 0  # stores the maximum length found
    max_str = ""

    # Try every possible starting point of the substring
    for i in range(n):
        seen = set()  # to store unique characters in current substring

        # Try to extend the substring as far as we can without repeating
        for j in range(i, n):
            if s[j] in seen:
                break  # found a repeating character, stop expanding
            seen.add(s[j])  # add current character to the set
            current_length = j - i + 1  # calculate current length
            if current_length > max_len:  # update max length and substring
                max_len = current_length
                max_str = s[i:j + 1]  # include the current character
    return max_len, max_str  # return the maximum length and the longest substring

s = "abcabcbb"
length, substring = lengthOfLongestSubstring(s)

'''
🧠 Time and Space Complexity:
Time: O(n²) – You check all substrings starting at every index

Space: O(k) – where k is the size of the set (at most 26 for lowercase, 128 for ASCII)
'''

# Optimal Approach

def lengthOfLongestSubstring(s):
    n = len(s)
    left = 0  # Left pointer of the sliding window
    right = 0  # Right pointer of the sliding window
    char_set = set()  # Set to store unique characters in current window
    max_len = 0  # Variable to store the maximum length of substring
    max_str = ""
    # Iterate using the right pointer
    while right < n:
        if s[right] not in char_set:
            # If character not in set, add it to the set
            char_set.add(s[right])
            current_length = right - left + 1  # calculate current length
            # Update max_len if the current window is longer
            if current_length > max_len:  # update max length and substring
                max_len = current_length
                max_str = s[left:right + 1]  # include the current character
            # Move right pointer to expand the window
            right += 1
        else:
            # If character already in set, remove character at left pointer
            char_set.remove(s[left])
            # Move left pointer to shrink the window
            left += 1
    return max_len, max_str  # return the maximum length and the longest substring

s = "abcabcbb"
length, substring = lengthOfLongestSubstring(s)

'''
🧠 Time Complexity:
O(n)
Each character is visited at most twice:

Once by the right pointer (when expanding the window)

Once by the left pointer (when removing duplicates)

So, total time is O(n) where n = len(s).

💾 Space Complexity:
O(k)
Where k is the size of the character set (in the worst case, all characters are unique):

For lowercase letters: O(26)

For ASCII: O(128)

For Unicode: O(number of unique characters)

The set stores at most k characters at a time → O(k) extra space.
'''