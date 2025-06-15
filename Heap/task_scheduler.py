# Brute Force Approach

def leastInterval(tasks, n):
    # Step 1: Count the frequency of each task
    task_freq = {}
    for task in tasks:
        task_freq[task] = task_freq.get(task, 0) + 1  # Increment the count for each task

    # Step 2: Create a list of (negative frequency, task) pairs
    max_list = []
    for task in task_freq:
        count = task_freq[task]         
        pair = (-count, task)  # Store negative frequency to simulate max-heap behavior
        max_list.append(pair)  
    max_list.sort()  # Sort the list to have the most frequent tasks at the front

    # Step 3: Initialize a cooldown list to manage tasks in cooldown
    cooldown_list = []
    time = 0  # Initialize time counter

    # Step 4: Process tasks until both lists are empty
    while max_list or cooldown_list:
        time += 1  # Increment time for each unit of time

        # Step 5: Process the most frequent task if available
        if max_list:
            freq, task = max_list.pop(0)  # Get the task with the highest frequency
            freq += 1  # Decrease the frequency (remember it's stored as negative)

            # If the task still has remaining frequency, add it to the cooldown list
            if freq != 0:
                cooldown_list.append((freq, task, time + n))  # (remaining frequency, task, time it can be used again)

        # Step 6: Check if any task in the cooldown list is ready to be processed
        if cooldown_list and cooldown_list[0][2] == time:
            ready_task = cooldown_list.pop(0)  # Get the task that is ready to be processed
            max_list.append((ready_task[0], ready_task[1]))  # Add it back to the max list
            max_list.sort()  # Sort the max list again to maintain order based on frequency

    return time  # Return the total time taken to complete all tasks

tasks = ["A","A","A","B","B","B"]
n = 2
ans = leastInterval(tasks, n)

'''
🕒 Time Complexity (TC):
Let:

n = number of total tasks.

k = number of unique tasks.

T = total time units the scheduler runs (can be up to n + idle slots).

Step-by-step:
Building task_freq dictionary:
O(n)

Constructing and sorting max_list initially:

List creation: O(k)

Sorting: O(k log k)

Main loop runs for T time units:

In each unit:

Pop from front of max_list: O(1)

Append to cooldown_list: O(1)

When a task returns from cooldown:

Append to max_list: O(1)

Sort max_list again: O(k log k) worst-case (if all tasks still have non-zero frequency)

⚠️ Sorting max_list every time a task returns is expensive.

So if cooldown happens often, and k tasks are live frequently, worst-case sort can happen up to n times.

➤ Worst-case time complexity:
O(n + k log k + T × k log k)
But T can go up to 2n in worst-case (due to idles), so:

✅ Final worst-case TC:
O(n × k log k)

🧠 Space Complexity (SC):
task_freq dictionary → O(k)

max_list (at most k entries) → O(k)

cooldown_list (at most k entries at any time) → O(k)

✅ Final Space Complexity:
O(k)
'''

# Optimal Approach

import heapq
from collections import deque

def leastInterval(tasks, n):
    # Step 1: Count the frequency of each task
    task_freq = {}
    for task in tasks:
        task_freq[task] = task_freq.get(task, 0) + 1  # Increment the count for each task

    # Step 2: Create a max heap based on negative frequencies for max behavior
    maxHeap = []
    for task, count in task_freq.items():
        heapq.heappush(maxHeap, (-count, task))  # Push negative count to simulate max heap

    # Step 3: Initialize a queue to manage tasks during their cooldown period
    cooldown_queue = deque()  # Queue to hold tasks that are in cooldown

    time = 0  # Initialize the time counter

    # Step 4: Process tasks until all are scheduled
    while maxHeap or cooldown_queue:
        time += 1  # Increment time for each cycle

        # Step 5: If there are tasks available in the max heap, process one
        if maxHeap:
            freq, task = heapq.heappop(maxHeap)  # Get the task with the highest frequency
            freq += 1  # Increment frequency (since it's stored as negative)

            # Step 6: If there are remaining instances of this task, add it to the cooldown queue
            if freq != 0:
                cooldown_queue.append((freq, task, time + n))  # Store the task and the time it can be re-added

        # Step 7: Check if any task in the cooldown queue is ready to be re-added to the heap
        if cooldown_queue and cooldown_queue[0][2] == time:
            ready_task = cooldown_queue.popleft()  # Remove the task from the queue
            heapq.heappush(maxHeap, (ready_task[0], ready_task[1]))  # Re-add the task to the max heap

    return time  # Return the total time taken to complete all tasks

tasks = ["A","A","A","B","B","B"]
n = 2
ans = leastInterval(tasks, n)

'''
Time Complexity: O(n) + O(nlogn) + O(nlogn)
Space Complexity: O(n) + O(n) + O(n)
'''