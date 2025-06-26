# Brute Force Approach

def isValid(s):
    # Keep removing matching brackets until nothing changes
    while "()" in s or "{}" in s or "[]" in s:
        s = s.replace("()", "")
        s = s.replace("{}", "")
        s = s.replace("[]", "")
    
    # If everything is removed, it's valid
    return s == ""

s = "(]"
ans = isValid(s)

'''
Time Complexity: O(n)
Space Complexity: O(1)
'''

# Optimal Approach

from collections import deque
def isValid(s):
    stack = deque()
    bracket_map = {'(': ')', '{': '}', '[': ']'}
    
    for char in s:
        if char in bracket_map:  # opening bracket
            stack.append(char)
        elif char in bracket_map.values():  # closing bracket
            if not stack or bracket_map[stack.pop()] != char:
                return False
        else:
            return False  # invalid character

    return not stack  # True if all matched

s = "()[]{}"
ans = isValid(s)

'''
Time Complexity: O(n)
Space Complexity: O(n)
'''