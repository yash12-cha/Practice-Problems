'''
Intuition:

-> Calculate S1 = sum of numbers from 1 to n using formula n*(n+1)/2
-> Calculate S2 = sum of squares of numbers from 1 to n using formula n*(n+1)*(2n+1)/6
-> Find actual sum and sum of squares by traversing the array
-> Let x be missing number and y be repeating number
-> First equation: x - y = (expected sum - actual sum)
-> Second equation: x² - y² = (expected sum of squares - actual sum of squares)
-> Use these equations to solve for x and y

'''

def findTwoElement(a):
    n = len(a)

    # Expected sum and sum of squares for first n natural numbers
    expected_sum = (n * (n + 1)) // 2
    expected_sum_sq = (n * (n + 1) * (2 * n + 1)) // 6

    # Actual sum and sum of squares from the array
    actual_sum = sum(a)
    actual_sum_sq = sum(x * x for x in a)

    # Let X = repeating number, Y = missing number
    diff_sum = actual_sum - expected_sum              # X - Y
    diff_sum_sq = actual_sum_sq - expected_sum_sq     # X^2 - Y^2

    # X + Y = (X^2 - Y^2) / (X - Y) = diff_sum_sq / diff_sum
    sum_xy = diff_sum_sq // diff_sum

    # Solving the equations:
    # X = (diff_sum + sum_xy) // 2
    # Y = X - diff_sum
    x = (diff_sum + sum_xy) // 2
    y = x - diff_sum

    return [x, y]

nums = [4, 3, 6, 2, 1, 1]
ans = findTwoElement(nums)


'''
Time Complexity: O(N), where N = the size of the given array.
Reason: We are using only one loop running for N times. So, the time complexity will be O(N).

Space Complexity: O(1) as we are not using any extra space to solve this problem.
'''