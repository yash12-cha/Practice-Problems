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