'''
Intuition:
-> By sorting the strings, the most different strings move to the ends.
-> So, the common prefix between the first and last strings in the sorted list is guaranteed to be the longest common prefix for the whole array.
-> We just compare these two character by character to find the result.
'''
def longestCommonPrefix(strs):
    if not strs:
        return ''
    strs.sort()
    first = strs[0]
    last = strs[-1]
    prefix = ''
    for i in range(len(first)):
        if i >= len(last) or first[i] != last[i]:
            break
        prefix += first[i]
    return prefix

strs = ["flower","flow","flight"]
ans = longestCommonPrefix(strs)

'''
✅ Time Complexity: O(N log N + M)
Where:

N = number of strings in the list

M = length of the shortest string (or more precisely, the length of the common prefix between the first and last strings after sorting)

Breakdown:

O(N log N) for sorting the list of strings.

O(M) for comparing the first and last strings character by character to build the prefix.

✅ Space Complexity: O(1)
'''