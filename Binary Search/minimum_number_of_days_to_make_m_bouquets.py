# Brute Force Approach


def minDays(bloomDay, m, k):
    # Check if it's possible to form m bouquets with k flowers each
    if len(bloomDay) < m * k:
        return -1  # Not enough flowers to make the required bouquets
    # Determine the minimum and maximum bloom days
    min_day = min(bloomDay)
    max_day = max(bloomDay)
    answer = -1  # Initialize answer to -1 (indicating no valid day found)
    # Iterate through each possible day from min_day to max_day
    for day in range(min_day, max_day + 1):
        bouquets = 0  # Count of bouquets that can be formed by the current day
        flowers_in_bouquet = (
            0  # Count of consecutive flowers that have bloomed
        )
        # Check each flower's bloom day
        for bloom in bloomDay:
            if bloom <= day:
                # Flower has bloomed by the current day
                flowers_in_bouquet += 1
                if flowers_in_bouquet == k:
                    # Form a bouquet if we have k consecutive flowers
                    bouquets += 1
                    flowers_in_bouquet = 0  # Reset for the next bouquet
            else:
                # Reset the count if the flower hasn't bloomed yet
                flowers_in_bouquet = 0
        # If we can form at least m bouquets, update the answer and break
        if bouquets >= m:
            answer = day
            break  # No need to check further days, we found a valid one
    return answer  # Return the earliest day found or -1 if not found


bloomDay = [1, 10, 3, 10, 2]
m = 3
k = 1
ans = minDays(bloomDay, m, k)


"""
Time Complexity (TC):
The time complexity of this approach is O(n * d), where:
n is the number of flowers (length of bloomDay).
d is the range of days from min_day to max_day. In the worst case, this could be as large as the difference between the maximum and minimum bloom days.

Space Complexity (SC):
The space complexity is O(1), as we are using a constant amount of extra space regardless of the input size. The variables used do not depend on the size of the input.
"""

# Optimal Approach


def getbouquet(bloomDay, day, k):

    bouquets = 0  # Initialize bouquet count
    flowers_in_bouquet = 0  # Initialize count of consecutive flowers

    # Iterate through each flower's bloom day
    for bloom in bloomDay:
        if bloom <= day:
            # Flower has bloomed by the current day
            flowers_in_bouquet += 1
            if flowers_in_bouquet == k:
                # Form a bouquet if we have k consecutive flowers
                bouquets += 1
                flowers_in_bouquet = 0  # Reset for the next bouquet
        else:
            # Reset the count if the flower hasn't bloomed yet
            flowers_in_bouquet = 0

    return bouquets  # Return the total number of bouquets formed


def minDays(bloomDay, m, k):

    # Check if it's possible to form m bouquets with k flowers each
    if len(bloomDay) < m * k:
        return -1  # Not enough flowers to make the required bouquets

    answer = -1  # Initialize answer to -1 (indicating no valid day found)
    low = min(bloomDay)  # The earliest possible bloom day
    high = max(bloomDay)  # The latest possible bloom day

    # Perform binary search on the range of bloom days
    while low <= high:
        mid = (low + high) // 2  # Calculate the middle day
        bouquets = getbouquet(
            bloomDay, mid, k
        )  # Count bouquets that can be formed by mid day

        if bouquets >= m:
            answer = mid  # Found a valid day, try for an earlier day
            high = mid - 1  # Search for a smaller day
        else:
            low = mid + 1  # Search for a larger day

    return answer  # Return the earliest day found or -1 if not found


bloomDay = [1, 10, 3, 10, 2]
m = 3
k = 1
ans = minDays(bloomDay, m, k)

"""
Time Complexity (TC):
The time complexity of this approach is O(n log d), where:
n is the number of flowers (length of bloomDay).
d is the range of days from min(bloomDay) to max(bloomDay). The binary search runs in 
O(log d), and for each day checked, the getbouquet function runs in O(n)

Space Complexity (SC):
The space complexity is O(1), as we are using a constant amount of extra space regardless of the input size. The variables used do not depend on the size of the input.
"""
