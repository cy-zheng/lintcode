class Solution:
    # @param nums {int[]} an array of integer
    # @param target {int} an integer
    # @return {int} an integer
    def twoSum5(self, nums, target):
        # Write your code here
        nums.sort()
        result = 0
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left] + nums[right] <= target:
                result += right - left
                left += 1
            elif nums[right] + nums[left] > target:
                right -= 1
                
        return result