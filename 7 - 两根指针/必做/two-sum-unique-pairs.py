class Solution:
    # @param nums {int[]} an array of integer
    # @param target {int} an integer
    # @return {int} an integer
    def twoSum6(self, nums, target):
        # Write your code here
        result = 0
        if not nums or target is None:
            return result
        nums.sort()
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[right] + nums[left] == target:
                result += 1
                left += 1
                right -= 1
                while left < len(nums) and nums[left] == nums[left - 1]:
                    left += 1
                while right >= 0 and nums[right] == nums[right + 1]:
                    right -= 1
            elif nums[right] + nums[left] > target:
                right -= 1
            else:
                left += 1
                
        return result
        