import sys
class Solution:
    # @param {int[]} nums an array of integers
    # @param {int} k an integer
    # @return {int} the largest sum
    def maxSubarray4(self, nums, k):
        # Write your code here
        if len(nums) < k:
            return 0
        result = -sys.maxint - 1
        min_pre = sys.maxint
        prefix = [0]
        for i in range(len(nums)):
            prefix.append(nums[i] + prefix[-1])
            if i < k - 1:
                continue
            min_pre = min(prefix[i - k + 1], min_pre)
            result = max(prefix[-1] - min_pre, result)
        return result
            