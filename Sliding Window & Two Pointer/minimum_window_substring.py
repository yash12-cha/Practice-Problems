# Brute Force Approach


def smallestWindow(s1, s2):
    min_length = float("inf")  # Initialize to infinity
    min_window = ""  # To store the minimum window substring
    # Iterate through all possible starting points in s1
    for i in range(len(s1)):
        hash_map = {}

        # Build the frequency map for s2
        for char in s2:
            hash_map[char] = hash_map.get(char, 0) + 1

        cnt = 0  # Count of characters matched

        # Iterate through s1 starting from index i
        for j in range(i, len(s1)):
            if s1[j] in hash_map:
                if hash_map[s1[j]] > 0:
                    cnt += 1
                hash_map[s1[j]] -= 1

            # Check if we have matched all characters in s2
            if cnt == len(s2):
                # Update the minimum window if the current window is smaller
                current_length = j - i + 1
                if current_length < min_length:
                    min_length = current_length
                    min_window = s1[i : j + 1]

                # Break the loop since we found a valid window
                break
    return min_window


s1 = "ADOBECODEBANC"
s2 = "ABC"
ans = smallestWindow(s1, s2)

"""
Time Complexity: 
O(n^2 . m), where n is the length of s1 and m is the length of s2. This is due to the nested loops.

Space Complexity: 
O(m) for the frequency map of s2.
"""

# Optimal Approach


def smallestWindow(s1, s2):
    # Dictionary to store the frequency of characters in s2
    hash_map = {}
    left = 0  # Left pointer for the sliding window
    right = 0  # Right pointer for the sliding window
    cnt = 0  # Count of characters matched from s2
    min_length = float("inf")  # Initialize minimum length to infinity
    min_start = 0  # Start index of the minimum window

    # Build frequency map for characters in s2
    for char in s2:
        hash_map[char] = hash_map.get(char, 0) + 1

    # Expand the window by moving the right pointer
    while right < len(s1):
        # If the current character is in the hash_map
        if s1[right] in hash_map:
            # If the character count is still positive, we have a match
            if hash_map[s1[right]] > 0:
                cnt += 1
            # Decrease the count of the current character in the hash_map
            hash_map[s1[right]] -= 1

        # When we have a valid window containing all characters from s2
        while cnt == len(s2):
            # Update the minimum length and starting index if the current window is smaller
            if right - left + 1 < min_length:
                min_length = right - left + 1
                min_start = left

            # Try to contract the window from the left
            if s1[left] in hash_map:
                # Increase the count of the left character in the hash_map
                hash_map[s1[left]] += 1
                # If the count goes back to positive, we lose a match
                if hash_map[s1[left]] > 0:
                    cnt -= 1

            # Move the left pointer to the right to shrink the window
            left += 1

        # Move the right pointer to expand the window
        right += 1

    # If min_length was updated, return the smallest window substring; otherwise, return an empty string
    return (
        ""
        if min_length == float("inf")
        else s1[min_start : min_start + min_length]
    )


"""
📊 Time & Space Complexity:
O(|s1| + |s2|) We iterate through s2 once to build req. Then we traverse s1 with two pointers. Each pointer moves at most |s1| times. Overall, it’s O(n + m) ≈ O(n) 

Space Complexity: O(1)
"""
