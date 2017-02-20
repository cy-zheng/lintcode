class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number 
             and the index of the last number
    """
    def subarraySum(self, nums):
        # write your code here
        prefix = [0]
        cache = {0: 0}
        for i in range(len(nums)):
            temp = prefix[-1] + nums[i]
            if temp in cache:
                return [cache[temp], i]
            prefix.append(temp)
            cache[temp] = i + 1