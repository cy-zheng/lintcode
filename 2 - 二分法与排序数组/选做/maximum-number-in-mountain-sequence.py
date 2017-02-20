class Solution:
    # @param {int[]} nums a mountain sequence which increase firstly and then decrease
    # @return {int} then mountain top
    def mountainSequence(self, nums):
        # Write your code here
        if len(nums) == 1:
            return nums[0]
        left = 0
        right = len(nums) - 1
        
        while left + 1 < right:
            mid = (right - left) / 2 + left
            if nums[mid - 1] < nums[mid] and nums[mid] < nums[mid + 1]:
                left = mid
            elif nums[mid - 1] > nums[mid] and nums[mid] > nums[mid + 1]:
                right = mid
            else:
                return nums[mid]
        return nums[left] if nums[left] > nums[right] else nums[right]
                