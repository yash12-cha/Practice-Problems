// Brute force approach

/* 
x & (x - 1) == 0  ----> Only true if x is power of 2 

Example:
x = 8     → 1000
x-1 = 7   → 0111
1000 & 0111 = 0000 → true

Non-example:
x = 6     → 0110
x-1 = 5   → 0101
0110 & 0101 = 0100 → not 0 → false
*/

func isPowerOfTwo(x int) bool {
    // Powers of 2 are always positive
    if x <= 0 {
        return false
    }

    // Only powers of 2 satisfy this bitwise condition
    if (x & (x - 1)) == 0 {
        return true
    }else {
        return false
    }
}

func countPairs(deliciousness []int) int {
    cnt := 0
    for i := 0; i < len(deliciousness); i++{
        for j := i+1; j < len(deliciousness); j++{
            sum := deliciousness[i] + deliciousness[j]
            if isPowerOfTwo(sum){
                cnt++
            }
        }
    }
    return cnt
}

/*
Time Complexity = O(n²)
Space Complexity = O(1)
*/