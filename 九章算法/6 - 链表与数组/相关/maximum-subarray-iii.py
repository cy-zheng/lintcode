import sys
class Solution:
    """
    @param nums: A list of integers
    @param k: An integer denote to find k non-overlapping subarrays
    @return: An integer denote the sum of max k non-overlapping subarrays
    """
    def maxSubArray(self, nums, k):
        # write your code here
        dp = [[-sys.maxint - 1 for i in xrange(len(nums))] for j in xrange(k)]
        for j in xrange(len(nums)):
            dp[0][j] = self.maxSubArrayI(nums, 0, j + 1)[0]
        for i in xrange(1, k):
            for j in xrange(i, len(nums)):
                max_array = self.maxSubArrayI(nums, i, j + 1)
                max_result = -sys.maxint - 1
                for _ in xrange(i - 1, j):
                    max_result = max(max_result, dp[i - 1][_] + max_array[_ - i + 1])
                dp[i][j] = max_result
        return dp[-1][-1]
                
    def maxSubArrayI(self, nums, start, end):
        prefix = [0]
        min_pre = sys.maxint
        result = -sys.maxint - 1
        results = []
        for n in nums[start:end][::-1]:
            min_pre = min(min_pre, prefix[-1])
            prefix.append(prefix[-1] + n)
            if prefix[-1] - min_pre > result:
                result = prefix[-1] - min_pre
            results.append(result)
        return results[::-1]