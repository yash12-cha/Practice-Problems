'''
Approach:
Keep iterating while the power is greater than zero. If the power is odd, multiply the current result (ans) by x and reduce the power by 1. Otherwise, if the power is even, square x (i.e., multiply x by itself) and halve the power. Repeat these steps until the power becomes zero. At the end, ans will hold the final result.
'''
def myPow(x ,n):
    ans = 1
    power = n
    
    # Handle negative powers by inverting x and making power positive
    if n < 0:
        x = 1 / x
        power = -n
    # Exponentiation by squaring
    while power > 0:
        # If power is even, square the base and halve the power
        if power % 2 == 0:
            x = x * x
            power = power // 2
        else:
            # If power is odd, multiply ans by the base and decrease power by 1
            ans = ans * x
            power = power - 1
    return ans

x = 2.00000
n = 10
ans = myPow(x, n)

'''
Time Complexity: O(log n)
Space Complexity: O(1)
'''