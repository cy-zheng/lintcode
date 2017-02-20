class Solution:
    # @param nums {int[]} a list of integers
    # @param k {int} size of window
    # @return {int[]} the sum of element inside the window at each moving
    def winSum(self, nums, k):
        # Write your code here
        result = []
        if not nums or not k or len(nums) < k:
            return result
        
        result.append(sum(nums[:k]))
        for i in range(k, len(nums)):
            result.append(nums[i] + result[-1] - nums[i - k])
            
        return result