'''
Approach:
-> Splitting the string s into a list of words using split(), which automatically removes any extra spaces.
-> Iterating over the list in reverse using a for loop and range(len - 1, -1, -1) to build a new list cleaned_words.
-> Joining the reversed words with a single space to form the final result.
So instead of reversing characters, it focuses on reversing the order of words using index-based iteration.
'''

def reverseWords(s):
    words = s.split()
    cleaned_words = []
    for i in range(len(words) - 1, -1, -1):
        cleaned_words.append(words[i])
    ans = ' '.join(cleaned_words)
    return ans
s = "the sky is blue"
ans = reverseWords(s)

'''
Time Complexity: O(N), Traversing the entire string
Space Complexity: O(N)
'''