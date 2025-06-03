'''
Approach:
We assume the first string is the base for the common prefix, then compare each character of it with the same position in all other strings.
As soon as a mismatch or shorter string is found, we return the prefix built so far.
This works because the common prefix must be common across all strings starting from index 0.
'''
def longestCommonPrefix(strs):
    # Return empty string if input list is empty
    if not strs:
        return ""

    prefix = ""

    # Loop through characters of the first string
    for i in range(len(strs[0])):
        char = strs[0][i]  # Get the i-th character of the first string

        # Check if this character is present at the same position in all other strings
        for j in range(1, len(strs)):
            # If the current string ends or the character at index i doesn't match, return the prefix found so far
            if i >= len(strs[j]) or strs[j][i] != char:
                return prefix

        # If all characters matched at this position, add to prefix
        prefix += char

    return prefix

strs = ["flower","flow","flight"]
ans = longestCommonPrefix(strs)

'''
✅ Time Complexity: O(N * M)
Where:

N = number of strings in the list strs

M = length of the shortest string in the list

Why?

In the worst case, we compare each character of the shortest string (M characters) with all N strings.

So total comparisons in the worst case = N * M

✅ Space Complexity: O(1)
We're only using a few extra variables (prefix, char, loop counters).

No additional data structures are used that grow with input size.

Hence, auxiliary space is constant.
'''
