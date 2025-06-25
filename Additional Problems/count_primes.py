def isPrime(n: int) -> bool:
    """
    Check if an integer n is prime.
    Returns True if n > 1 and has no divisors other than 1 and itself.
    """
    if n <= 1:
        return False  # 0 and 1 are not primes

    # Test potential divisors from 2 up to n-1 (brute force)
    for i in range(2, n):
        if n % i == 0:
            return False  # Found a divisor → not prime

    return True  # No divisors found → prime


def countPrimes(n: int) -> int:
    """
    Count how many primes are strictly less than n
    using the brute-force prime check.
    """
    count = 0
    for i in range(2, n):
        if isPrime(i):
            count += 1
    return count


# Example usage:
n = 10
ans = countPrimes(n)


'''
Time Complexity: O(n * n)

Space Complexity: O(1)
'''

import math
def isPrime(n: int) -> bool:
    # Corner case
    if n <= 1 :
        return False

    # Check divisibility from 2 up to √n
    limit = int(math.sqrt(n))
    for i in range(2, limit+1):
        if n % i == 0:
            return False  # Found a divisor → not prime

    return True  # No divisors found → prime

def countPrimes(n: int) -> int:
    cnt = 0
    for i in range(2, n):
        if isPrime(i):
            cnt += 1
    return cnt

# Example usage:
n = 10
ans = countPrimes(n)

'''
Time Complexity: O(n * √n)

Space Complexity: O(1)
'''

from math import sqrt

def countPrimes(n: int) -> int:
    # If n is less than 2, there are no prime numbers
    if n < 2:
        return 0
    
    # Create a list to track prime status for each number from 0 to n-1
    # Initially, assume all numbers are prime (True)
    primes = [True] * n
    
    # 0 and 1 are not prime numbers
    primes[0] = primes[1] = False
    
    # Iterate from 2 to the square root of n
    for i in range(2, int(sqrt(n)) + 1):
        # If i is still marked as prime
        if primes[i]:
            # Mark all multiples of i as not prime, starting from i*i
            for j in range(i * i, n, i):
                primes[j] = False
    
    # Return the count of prime numbers by summing the True values in the primes list
    return sum(primes)

# Example usage:
n = 10
ans = countPrimes(n)

'''
Time Complexity: O(n*log(log(n)))
Space Complexity: O(n)
'''

