# Brute Force Approach

def findSmallestMaxDist(stations, k):
    
    # Initialize an array to keep track of how many additional stations are added between each pair of existing stations
    how_many = [0] * (len(stations) - 1)

    # Add k stations
    for _ in range(k):
        max_val = -1  # Initialize the maximum section length
        max_val_indx = -1  # Index of the section where the maximum length occurs

        # Iterate through each section between existing stations
        for i in range(len(stations) - 1):
            # Calculate the distance between the current pair of stations
            diff = stations[i + 1] - stations[i]
            # Calculate the length of each section if we add one more station
            section_len = diff / (how_many[i] + 1)

            # Update max_val and max_val_indx if we find a larger section length
            if max_val < section_len:
                max_val = section_len
                max_val_indx = i

        # Increment the count of additional stations for the section with the maximum length
        how_many[max_val_indx] += 1

    # Calculate the maximum distance after adding the stations
    max_ans = -1
    for i in range(len(stations) - 1):
        diff = stations[i + 1] - stations[i]
        section_len = diff / (how_many[i] + 1)  # Calculate the new section length
        max_ans = max(max_ans, section_len)  # Update the maximum distance

    return max_ans  # Return the smallest maximum distance

stations =  [176, 274, 498, 586, 1184, 1596, 1622, 2065, 2371, 2440, 2749, 2863, 3343, 3451, 3582, 4022, 4089, 4491, 4618, 4678, 4787, 5407, 6217, 6425, 6740, 7013, 7682, 8736, 8771, 8984, 9145, 9320, 9449, 9511, 9641, 9661, 9738, 10369, 10374, 10443, 10571, 10913, 11238, 11420, 11448, 11483, 12762, 12875, 12880, 13038, 13128, 13282, 13391, 13573, 13615, 13657, 13897, 13940, 14213, 14272, 14513, 14749, 15451, 15719, 15733, 16027, 16219, 16543, 16577, 16590, 16805, 16825, 17053, 17238, 17273, 17580, 17723, 17725, 18026, 18528, 19370, 19371, 19382, 19754, 19852, 19935, 20066, 20154, 20278, 20748, 20827, 20941, 20982, 21000, 21068, 21306, 21422, 21893, 22269, 22359, 22562, 22596, 22642, 22802, 23196, 23387, 23634, 23797, 23815, 24143, 24655, 24679, 25044, 25846, 26281, 26287, 26346, 26667, 26675, 26817, 26982, 27409, 27601, 29652, 29772, 30070, 30587, 30622, 31462, 31611, 31662, 31686, 31948]
k = 1638
ans = findSmallestMaxDist(stations, k)

'''
Time Complexity: O(k*n) + O(n), n = size of the given array, k = no. of gas stations to be placed.
Reason: O(k*n) to insert k gas stations between the existing stations with maximum distance. Another O(n) for finding the answer i.e. the maximum distance.

Space Complexity: O(n-1) as we are using an array to keep track of placed gas stations.
''' 

# Another Approach

import heapq

'''
We use the heapq module to implement a heap in Python. By default, it provides a Min Heap. 
To use it as a Max Heap, we insert the negative of each value (i.e., multiply each value by -1). 
When retrieving values, we again multiply by -1 to get the original values.
'''

def findSmallestMaxDist(stations, k):
    
    # Initialize an array to keep track of how many additional stations are added between each pair of existing stations
    how_many = [0] * (len(stations) - 1)
    
    # Create a max-heap to store the distances between stations
    maxHeap = []

    # Using heapify to convert list into heap
    heapq.heapify(maxHeap)
    
    # Populate the heap with the initial distances between each pair of stations
    for i in range(len(stations) - 1):
        heapq.heappush(maxHeap, ((-1)*(stations[i + 1] - stations[i]), i))
    
    # Add k additional stations
    for _ in range(1, k+1):
        # Pop the largest distance from the heap
        tp = heapq.heappop(maxHeap)
        sec_ind = tp[1]  # Index of the section with the largest distance
        
        # Increment the count of additional stations for this section
        how_many[sec_ind] += 1
        
        # Calculate the new section length after adding a station
        initial_diff = stations[sec_ind + 1] - stations[sec_ind]
        new_sec_len = initial_diff / (how_many[sec_ind] + 1)
        
        # Push the updated section length back into the heap
        heapq.heappush(maxHeap, ((-1)*new_sec_len, sec_ind))
    
    # The smallest maximum distance is the largest distance in the heap (negated back to positive)
    value = maxHeap[0][0] *(-1)
    # Round the value to two decimal places, adding a small epsilon to handle floating-point precision issues
    rounded_value = round(value + 1e-8, 2)
    return rounded_value

stations =  [176, 274, 498, 586, 1184, 1596, 1622, 2065, 2371, 2440, 2749, 2863, 3343, 3451, 3582, 4022, 4089, 4491, 4618, 4678, 4787, 5407, 6217, 6425, 6740, 7013, 7682, 8736, 8771, 8984, 9145, 9320, 9449, 9511, 9641, 9661, 9738, 10369, 10374, 10443, 10571, 10913, 11238, 11420, 11448, 11483, 12762, 12875, 12880, 13038, 13128, 13282, 13391, 13573, 13615, 13657, 13897, 13940, 14213, 14272, 14513, 14749, 15451, 15719, 15733, 16027, 16219, 16543, 16577, 16590, 16805, 16825, 17053, 17238, 17273, 17580, 17723, 17725, 18026, 18528, 19370, 19371, 19382, 19754, 19852, 19935, 20066, 20154, 20278, 20748, 20827, 20941, 20982, 21000, 21068, 21306, 21422, 21893, 22269, 22359, 22562, 22596, 22642, 22802, 23196, 23387, 23634, 23797, 23815, 24143, 24655, 24679, 25044, 25846, 26281, 26287, 26346, 26667, 26675, 26817, 26982, 27409, 27601, 29652, 29772, 30070, 30587, 30622, 31462, 31611, 31662, 31686, 31948]
k = 1638
ans = findSmallestMaxDist(stations, k)

'''
Time Complexity: O(nlogn + klogn),  n = size of the given array, k = no. of gas stations to be placed.
Reason: Insert operation of priority queue takes logn time complexity. O(nlogn) for inserting all the indices with distance values and O(klogn) for placing the gas stations.

Space Complexity: O(n-1)+O(n-1)
Reason: The first O(n-1) is for the array to keep track of placed gas stations and the second one is for the priority queue.
'''