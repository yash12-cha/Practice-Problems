# Brute Force Approach

def getAssignCnt(arr, i):
    student_cnt = 1  # Initialize the number of students to 1
    page_cnt = 0  # Initialize the number of pages assigned to the current student to 0

    for ele in arr:  # Iterate through each book in the array
        if ele > i:  # If a single book has more pages than the maximum allowed
            return float('inf')  # Return infinity, indicating an impossible assignment

        if page_cnt + ele <= i:  # If the current book can be assigned to the current student
            page_cnt += ele  # Add the book's pages to the current student's page count
        else:  # If the current book cannot be assigned to the current student
            student_cnt += 1  # Assign a new student
            page_cnt = ele  # Assign the current book to the new student

    return student_cnt  # Return the total number of students required


def findPages(arr, k):

    if k > len(arr):  # If the number of students is greater than the number of books
        return -1  # Return -1, indicating an impossible assignment

    min_pages = float('inf')  # Initialize the minimum number of pages to infinity

    # Iterate through all possible values for the maximum number of pages a student can have
    for i in range(max(arr), sum(arr) + 1):
        student_needed = getAssignCnt(arr, i)  # Calculate the number of students needed for the current maximum page limit

        if student_needed <= k:  # If the number of students needed is less than or equal to the available students
            min_pages = min(min_pages, i)  # Update the minimum number of pages if the current value is smaller

    if min_pages == float('inf'):  # If no valid assignment was found
        return -1  # Return -1, indicating an impossible assignment
    else:
        return min_pages  # Return the minimum number of pages

arr = [12, 34, 67, 90]
k = 2
ans = findPages(arr, k)

'''
Time Complexity: O(N * (sum(arr)-max(arr)+1)), where N = size of the array, sum(arr) = sum of all array elements, max(arr) = maximum of all array elements.
Reason: We are using a loop from max(arr) to sum(arr) to check all possible values of time. Inside the loop, we are calling the countPainters() function for each number. Now, inside the countPainters() function, we are using a loop that runs for N times.

Space Complexity:  O(1) as we are not using any extra space to solve this problem.
'''

# Optimal Approach

def getAssignCnt(arr, i):
    student_cnt = 1
    page_cnt = 0
    for ele in arr:
        if ele > i:
            return float('inf')
        if page_cnt + ele <= i:
            page_cnt += ele
        else:
            student_cnt += 1
            page_cnt = ele
    return student_cnt
    
#Function to find minimum number of pages.
def findPages(arr, k):
    if k > len(arr):
        return -1
    low = max(arr)
    high = sum(arr)
    ans = -1
    while(low<=high):
        mid = (low+high)//2
        student_needed = getAssignCnt(arr, mid)
        if student_needed <= k:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
            
    return ans

arr = [12, 34, 67, 90]
k = 2
ans = findPages(arr, k)

'''
Time Complexity: O(N * log(sum(arr)-max(arr)+1)), where N = size of the array, sum(arr) = sum of all array elements, max(arr) = maximum of all array elements.
Reason: We are applying binary search on [max(arr), sum(arr)]. Inside the loop, we are calling the countPainters() function for the value of ‘mid’. Now, inside the countPainters() function, we are using a loop that runs for N times.

Space Complexity:  O(1) as we are not using any extra space to solve this problem.
'''