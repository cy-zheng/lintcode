class Solution:
    """
    @param nums: The integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, nums):
        # write your code here
        if not nums:
            return 0
        
        cache = [1 for i in range(len(nums))]
        
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i] and cache[i] < cache[j] + 1:
                    cache[i] = cache[j] + 1
                    
        return max(cache)
