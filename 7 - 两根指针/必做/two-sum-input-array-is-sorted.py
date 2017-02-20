class Solution:
    """
    @param nums {int[]} n array of Integer
    @param target {int} = nums[index1] + nums[index2]
    @return {int[]} [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, nums, target):
        # Write your code here
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[right] + nums[left] == target:
                return [left + 1, right + 1]
            elif nums[right] + nums[left] > target:
                right -= 1
            else:
                left += 1