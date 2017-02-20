class Solution:
    # @param {int[]} nums an integer array
    # @param {int} target an integer
    # @return {int} the difference between the sum and the target
    def twoSumClosest(self, nums, target):
        # Write your code here
        nums.sort()
        result = None
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[right] + nums[left] == target:
                return 0
            elif nums[right] + nums[left] > target:
                if result is None or abs(nums[right] + nums[left] - target) < result:
                    result = abs(nums[right] + nums[left] - target)
                right -= 1
            else:
                if result is None or abs(nums[right] + nums[left] - target) < result:
                    result = abs(nums[right] + nums[left] - target)
                left += 1
        return result