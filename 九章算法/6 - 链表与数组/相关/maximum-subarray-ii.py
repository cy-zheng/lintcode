import sys
class Solution:
    """
    @param nums: A list of integers
    @return: An integer denotes the sum of max two non-overlapping subarrays
    """
    def maxTwoSubArrays(self, nums):
        # write your code here    
        left = [-sys.maxint - 1]
        right = [-sys.maxint - 1]
        
        # find left part
        min_pre = sys.maxint
        prefix = [0]
        for i in xrange(len(nums) - 1):
            min_pre = min(min_pre, prefix[-1])
            prefix.append(prefix[-1] + nums[i])
            if prefix[-1] - min_pre > left[-1]:
                left.append(prefix[-1] - min_pre)
            else:
                left.append(left[-1])
                
        left = left[1:]
        
        # find right part
        min_pre = sys.maxint
        prefix = [0]
        for i in xrange(len(nums) - 1, 0, -1):
            min_pre = min(min_pre, prefix[-1])
            prefix.append(prefix[-1] + nums[i])
            if prefix[-1] - min_pre > right[-1]:
                right.append(prefix[-1] - min_pre)
            else:
                right.append(right[-1])
                
        right = right[1:][::-1]
        
        result = -sys.maxint - 1
        for i in range(len(left)):
            result = max(left[i] + right[i], result)
            
        return result
        