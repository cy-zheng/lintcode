class Solution:
    # @param {int[]} nums an array with positive and negative numbers
    # @param {int} k an integer
    # @return {double} the maximum average
    def maxAverage(self, nums, k):
        # Write your code here
        left, right = min(nums), max(nums)
        prefix = [0] * (len(nums) + 1)
        while right - left >= 1e-6:
            mid, check = (right + left) / 2.0, False
            min_pre = 0
            for i in xrange(1, len(nums) + 1):
                prefix[i] = prefix[i - 1] + nums[i - 1] - mid
                if i >= k and prefix[i] >= min_pre:
                    check = True
                    break
                if i >= k:
                    min_pre = min(min_pre, prefix[i - k + 1])
            if check:
                left = mid
            else:
                right = mid
        return left