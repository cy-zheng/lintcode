class Solution:
    # @param {int[]} nums a set of distinct positive integers
    # @return {int[]} the largest subset 
    def largestDivisibleSubset(self, nums):
        # Write your code here
        if not nums:
            return []
        
        nums.sort()
        cache = [1 for i in range(len(nums))]
        path = [-1 for i in range(len(nums))]
        
        for i in range(len(nums)):
            max_value = 1
            max_index = -1
            for j in range(i):
                if nums[i] % nums[j] == 0 and cache[j] + 1 > max_value:
                    max_value = cache[j] + 1
                    max_index = j
            cache[i] = max_value  
            path[i] = max_index
            
        index = cache.index(max(cache))
        result = [nums[index]]
        while path[index] != -1:
            index = path[index]
            result.append(nums[index])
        return result[::-1]
                    