class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2 
    @return: nothing
    """
    def sortColors(self, nums):
        # write your code here
        if not nums:
            return
        i = 0
        for color in range(0, 3):
            i = self.oneColor(nums, i, color)
        
    def oneColor(self, nums, index, color):
        left = index
        right = len(nums) - 1
        while left < right:
            while left < right and nums[left] == color:
                left += 1
            while left < right and nums[right] > color:
                right -= 1
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
        return left if nums[left] != color else left + 1