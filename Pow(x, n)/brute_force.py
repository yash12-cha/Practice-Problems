'''
Approach:  The idea is to simply multiply x exactly n times using a iterative loop.
'''

def myPow(x, n):
    ans = 1
    power = n
    # If n is negative, invert x to 1/x and make n positive.
    if n < 0:
        x = 1 / x
        power = -n
    for _ in range(power):
        ans = ans * x
    return ans

x = 2.00000
n = 10
ans = myPow(x, n)

'''
Time Complexity: O(N)
Space Complexity: O(1)
'''