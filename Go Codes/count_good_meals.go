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


// Optimal Approach

func countPairs(deliciousness []int) int {
    const MOD = 1_000_000_007
    maxSum := 0
    // Calculate the maximum possible sum to determine the power of twos
    for _, val := range deliciousness {
        if val > maxSum {
            maxSum = val
        }
    }
    maxSum *= 2 // The maximum sum can be twice the maximum value in deliciousness
    // Generate the list of powers of two up to maxSum
    powerOfTwos := []int{}
    for i := 1; i <= maxSum; i++ {
        if i & (i - 1) == 0 { // Check if i is a power of two
            powerOfTwos = append(powerOfTwos, i)
        }
    }
    // Map to count occurrences of each deliciousness value
    count := make(map[int]int)
    res := 0
    // Iterate through each value in deliciousness
    for _, val := range deliciousness {
        // Check for each power of two
        for _, target := range powerOfTwos {
            complement := target - val
            freq, exists := count[complement]
            if exists {
                // If it exists, freq will hold the number of times the complement has been seen
                // Update the result by adding the frequency of the complement
                res = (res + freq) % MOD // Ensure the result stays within the bounds of MOD
            }
        }
        count[val]++ // Increment the count for the current value
    }
    
    return res
}

/*
Time Complexity = O(n.log(maxValue))
Space Complexity = O(n)
*/


/*
Note:
In above code make() is used to initialize the map before using it, because in Go, maps must be explicitly initialized to allocate memory.
Without make, writing to the map would cause a runtime panic since it's nil.
*/