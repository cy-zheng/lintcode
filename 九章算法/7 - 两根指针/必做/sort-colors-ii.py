class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sortColors2(self, colors, k):
        # write your code here
        if not colors or k is None:
            return
        i = 0
        for color in range(1, k + 1):
            i = self.oneColor(colors, i, color)
        
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