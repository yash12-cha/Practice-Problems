def nthRoot(n ,x):
    ans = 1          # placeholder for current power comparison
    power = n        # exponent used to check against x

    # Handle negative n by converting to positive via reciprocal
    # (so we effectively compute x^(-1/n))
    if n < 0:
        x = 1 / x
        power = -n

    # Brute-force search: try all integer candidates i from 1 to x
    for i in range(1, x + 1):
        ans = i ** power        # compute iⁿ (or i^|n| for negative n)

        if ans == x:
            return i            # found exact integer root

        elif ans > x:
            break               # no need to try larger i; we've passed x

    return -1                   # no exact integer nth root found

n = 2
x = 9
ans = nthRoot(n, x)

'''
Time Complexity (TC):
The time complexity of the modified nthRoot function is O(x) in the worst case. This is because the function iterates from 1 to x to find the integer n-th root. In the worst case, it may need to check every integer up to x.

Space Complexity (SC):
The space complexity is O(1). The function uses a constant amount of extra space regardless of the input size, as it only uses a few variables (ans, power, and the loop variable i).
'''

def func(mid, n, m):
    ans = 1
    for i in range(1, n + 1):
        ans *= mid
        if ans > m:
            return 2  # mid^n exceeded m, no need to continue
    if ans == m:
        return 1
    return 0  # mid^n is less than m

def NthRoot(n, m):
    low = 1
    high = m

    while low <= high:
        mid = (low + high) // 2
        midN = func(mid, n, m)

        if midN == 1:
            # Found exact nth root
            return mid
        elif midN == 0:
            # mid^n < m, so try larger mid
            low = mid + 1
        else:
            # mid^n > m, so try smaller mid
            high = mid - 1

    # If no exact nth root found
    return -1

n = 2
m = 9
ans = nthRoot(n, m)

'''
Time Complexity: O(logN), N = size of the given array.
Reason: We are basically using binary search to find the minimum.

Space Complexity: O(1)
Reason: We have not used any extra data structures, this makes space complexity, even in the worst case as O(1).
'''