'''
🧠 Intuition:
Divide the list of strings into two halves.

Recursively find the longest common prefix in each half.

Merge results by comparing the two prefixes.
'''
def commonPrefix(str1, str2):
    result = ""
    min_len = min(len(str1), len(str2))
    for i in range(min_len):
        if str1[i] != str2[i]:
            break
        result += str1[i]
    return result

def longestCommonPrefixUtil(strs, left, right):
    if left == right:
        return strs[left]
    
    mid = (left + right) // 2
    lcpLeft = longestCommonPrefixUtil(strs, left, mid)
    lcpRight = longestCommonPrefixUtil(strs, mid + 1, right)
    
    return commonPrefix(lcpLeft, lcpRight)

def longestCommonPrefix(strs):
    if not strs:
        return ""
    return longestCommonPrefixUtil(strs, 0, len(strs) - 1)

strs = ["flower", "flow", "flight"]
ans = longestCommonPrefix(strs)

'''
🕒 Time Complexity:
O(N * M)

N: number of strings

M: average length of strings
(Each character may be compared multiple times but fewer than brute-force)

➡️ Space Complexity: O(log N * M)

Here's why:
Recursive Stack Depth: Since we divide the array into halves, the recursion depth is O(log N).

String Comparisons: At each recursion level, the commonPrefix function compares two strings up to M characters (where M is the max length of the prefix between them).

So:

Total auxiliary space = recursion depth × max string length = O(log N * M)
'''