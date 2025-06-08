# Brute Force Approach
def totalFruit(fruits):
    n = len(fruits)
    max_cnt = 0  # To track the maximum number of fruits collected in any valid subarray

    for i in range(n):
        cnt = 0  # Count of fruits collected in current subarray
        fruit_types = set()  # Set to store types of fruits in the current subarray

        for j in range(i, n):
            fruit_types.add(fruits[j])

            if len(fruit_types) <= 2:
                cnt += 1  # Valid fruit type, increase count
                max_cnt = max(max_cnt, cnt)  # Update max if needed
            else:
                break  # More than 2 fruit types not allowed, exit inner loop

    return max_cnt

fruits = [1,2,1]
ans = totalFruit(fruits)

'''
🧠 Time and Space Complexity:
Time: O(n²) — nested loops for each starting index.

Space: O(1) to O(2) — since at most 3 elements go into the set before breaking.
'''

# Optimal Approach
def totalFruit(fruits):
    count = {}       # Dictionary to store the count of each fruit type in the current window
    left = 0         # Left boundary of the sliding window
    max_fruits = 0   # Stores the maximum number of fruits collected with at most 2 types

    for right in range(len(fruits)):
        fruit = fruits[right]
        count[fruit] = count.get(fruit, 0) + 1  # Add current fruit to the window

        # If we have more than 2 types of fruits, shrink the window from the left
        while len(count) > 2:
            left_fruit = fruits[left]
            count[left_fruit] -= 1
            if count[left_fruit] == 0:
                del count[left_fruit]  # Remove fruit type if count becomes zero
            left += 1  # Shrink the window

        # Update the max length of valid window
        max_fruits = max(max_fruits, right - left + 1)

    return max_fruits

fruits = [1,2,1]
ans = totalFruit(fruits)

'''
🧠 Time and Space Complexity:
Time: O(n) — Each fruit is processed at most twice – once by right and once by left

Space: O(1) to O(2) — since at most 3 elements go into the set before breaking.
'''