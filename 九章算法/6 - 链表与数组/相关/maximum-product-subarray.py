import sys
class Solution:
    # @param nums: an integer[]
    # @return: an integer
    def maxProduct(self, nums):
        # write your code here
        min_pre_positive = 1
        min_pre_negative = 1
        prefix = [1]
        result = -sys.maxint - 1
        for n in nums:
            prefix.append(n * (prefix[-1] if prefix[-1] != 0 else 1))
            if n == 0:
                min_pre_positive = 1
                min_pre_negative = 1
            else:
                if prefix[-1] > 0:
                    min_pre_positive = min(min_pre_positive, prefix[-1])
                    result = max(prefix[-1] / min_pre_positive, result)
                else:
                    result = max(prefix[-1] / min_pre_negative, result)
                    min_pre_negative = prefix[-1] if min_pre_negative > 0 \
                                    else max(min_pre_negative, prefix[-1])
        return result
                