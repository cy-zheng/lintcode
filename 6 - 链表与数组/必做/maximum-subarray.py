class Solution:
    """
    @param nums: A list of integers
    @return: An integer denote the sum of maximum subarray
    """
    def maxSubArray(self, nums):
        # write your code here
        prefix = [0]
        min_pre = 99999999
        result = -99999999
        for n in nums:
            min_pre = min(min_pre, prefix[-1])
            prefix.append(prefix[-1] + n)
            if prefix[-1] - min_pre > result:
                result = prefix[-1] - min_pre
        return result