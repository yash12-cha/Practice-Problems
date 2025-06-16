# Brute Force Approach

def maxCombinations(K, nums1, nums2):
    sum_ = []
    for i in range(len(nums1)):
        for j in range(len(nums2)):
            sum_.append(nums1[i] + nums2[j])
    sum_.sort(reverse=True)
    top_k = []
    for i in range(K):
        top_k.append(sum_[i])
    return top_k

nums1 = [3, 2]
nums2 = [1, 4]
K = 2
ans = maxCombinations(K, nums1, nums2)

'''
Time Complexity:

- Nested Loops to Generate All Sums -> O(n * m)
- Sorting the Combined Sum List -> O(n * m * log(n * m))
- Collecting Top K Elements -> O(K)
'''