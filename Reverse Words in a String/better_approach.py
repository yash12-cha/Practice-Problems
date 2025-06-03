'''
Approach:
-> Use a stack to push all the words in a stack
-> Now, all the words of the string are present in the stack, but in reverse order
-> Pop elements of the stack one by one and add them to our answer variable. Remember to add a space between the words as well.
'''
from collections import deque
def reverseWords(s):
    stack = deque()
    word = ''
    
    for ch in s:
        if ch != ' ':
            word += ch
        elif word:
            stack.append(word)
            word = ''
    
    # Append the last word if any
    if word:
        stack.append(word)
    
    reversed_words = []
    while stack:
        reversed_words.append(stack.pop())
    
    return ' '.join(reversed_words)

s = "the sky is blue"
ans = reverseWords(s)

'''
Time Complexity: O(N), Traversing the entire string
Space Complexity: O(N), Stack and ans variable
'''