import sys
class Solution:
    """
    @param nums: A list of integers
    @return: An integer indicate the value of maximum difference between two
             Subarrays
    """
    def maxDiffSubArrays(self, nums):
        # write your code here
        left_max = [-sys.maxint - 1]
        right_max = [-sys.maxint - 1]
        left_min = [sys.maxint]
        right_min = [sys.maxint]
        
        # find left part
        min_pre = sys.maxint
        max_pre = -sys.maxint - 1
        prefix = [0]
        for i in xrange(len(nums) - 1):
            min_pre = min(min_pre, prefix[-1])
            max_pre = max(max_pre, prefix[-1])
            prefix.append(prefix[-1] + nums[i])
            if prefix[-1] - min_pre > left_max[-1]:
                left_max.append(prefix[-1] - min_pre)
            else:
                left_max.append(left_max[-1])
            if prefix[-1] - max_pre < left_min[-1]:
                left_min.append(prefix[-1] - max_pre)
            else:
                left_min.append(left_min[-1])
                
        left_max = left_max[1:]
        left_min = left_min[1:]
        
        # find right part
        min_pre = sys.maxint
        max_pre = -sys.maxint - 1
        prefix = [0]
        for i in xrange(len(nums) - 1, 0, -1):
            min_pre = min(min_pre, prefix[-1])
            max_pre = max(max_pre, prefix[-1])
            prefix.append(prefix[-1] + nums[i])
            if prefix[-1] - min_pre > right_max[-1]:
                right_max.append(prefix[-1] - min_pre)
            else:
                right_max.append(right_max[-1])
            if prefix[-1] - max_pre < right_min[-1]:
                right_min.append(prefix[-1] - max_pre)
            else:
                right_min.append(right_min[-1])
                
        right_max = right_max[1:][::-1]
        right_min = right_min[1:][::-1]
        
        result = -sys.maxint - 1
        for i in range(len(left_max)):
            result = max(left_max[i] - right_min[i], result)
            result = max(right_max[i] - left_min[i], result)
            
        return result
