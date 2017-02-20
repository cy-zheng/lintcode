class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number 
             and the index of the last number
    """
    def subarraySumClosest(self, nums):
        # write your code here
        prefix = [(0, 0)]
        for i in range(len(nums)):
            prefix.append((prefix[-1][0] + nums[i], i + 1))
            
        prefix = sorted(prefix, key = lambda p: p[0])
        min_sum = 999999999
        index = [0, 0]
        for i in range(len(prefix) - 1):
            if abs(prefix[i][0] - prefix[i + 1][0]) < min_sum:
                min_sum = abs(prefix[i][0] - prefix[i + 1][0])
                index = (prefix[i][1], prefix[i + 1][1] - 1) \
                        if prefix[i][1] < prefix[i + 1][1] else \
                        (prefix[i + 1][1], prefix[i][1] - 1)
                        
        return index