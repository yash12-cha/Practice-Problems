# Brute Force Approach

def isNStraightHand(hand, groupSize):
    # Check if the total number of cards can be evenly divided into groups of the specified size
    if len(hand) % groupSize != 0:
        return False

    # Count frequencies of each card
    freq_map = {}
    for card in hand:
        freq_map[card] = freq_map.get(card, 0) + 1  # Increment the count for each card

    # Sort the hand to try forming groups starting from the smallest card
    hand.sort()

    # Iterate through each card in the sorted hand
    for card in hand:
        if freq_map[card] == 0:
            continue  # Skip this card if it has already been used in a group

        # Try to form a group starting from this card
        for i in range(groupSize):
            # Check if the next card in the sequence is available
            if freq_map.get(card + i, 0) == 0:
                return False  # Cannot form a valid group if any card is missing
            freq_map[card + i] -= 1  # Use this card by decrementing its count

    return True  # All groups were successfully formed

# Example usage
hand = [1, 2, 3, 3, 4, 4, 5, 6]
groupSize = 4
ans = isNStraightHand(hand, groupSize)

'''
Time Complexity (TC):

The time complexity of this function is O(n logn), where n is the number of cards in the hand. 
This is due to the sorting step. The subsequent operations of counting and checking frequencies are 
O(n), but the sorting dominates the overall complexity.

Space Complexity (SC):
The space complexity is O(n) for the frequency map, which stores the count of each unique card in the hand. In the worst case, if all cards are unique, the space used will be proportional to the number of cards.
'''


import heapq

def isNStraightHand(hand, groupSize):
    # Check if the total number of cards can be evenly divided into groups of the specified size
    if len(hand) % groupSize != 0:
        return False

    # Count frequencies of each card
    freq_map = {}
    for card in hand:
        freq_map[card] = freq_map.get(card, 0) + 1  # Increment the count for each card

    # Initialize a min-heap to store the unique cards
    minHeap = []
    for freq in freq_map:
        heapq.heappush(minHeap, freq)  # Push each unique card into the heap

    # While there are cards in the heap
    while minHeap:
        start = minHeap[0]  # Get the smallest available card
        
        # Try to form a group starting from this card
        for i in range(groupSize):
            num = start + i
            if freq_map.get(num, 0) == 0:
                return False  # Cannot form a valid group if any card is missing
            freq_map[num] -= 1  # Use this card

            # If the count of this card reaches zero, remove it from the heap
            if freq_map[num] == 0:
                if num in minHeap:
                    minHeap.remove(num)  # Remove the card from the heap
                    heapq.heapify(minHeap)  # Re-heapify after removal

    return True  # All groups were successfully formed

# Example usage
hand = [1, 2, 3, 3, 4, 4, 5, 6]
groupSize = 4
ans = isNStraightHand(hand, groupSize)

'''
Time Complexity (TC):

The time complexity of this function is O(n logk), where n is the number of cards in the hand and k is the number of unique cards. This is due to the heap operations (insertion and removal) which take O(log k)time. 
The overall complexity is dominated by the heap operations.

Space Complexity (SC):

The space complexity is O(k) for the frequency map and the min-heap, where k is the number of unique cards in the hand. In the worst case, if all cards are unique, the space used will be proportional to the number of unique cards.
'''