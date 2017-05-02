class Solution:
    # @param nums: a list of integers
    # @return: nothing
    def partitionArray(self, nums):
        # write your code here
        if not nums:
            return
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] % 2 == 0:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
            else:
                left += 1
        