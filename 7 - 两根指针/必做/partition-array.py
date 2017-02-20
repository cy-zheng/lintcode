class Solution:
    """
    @param nums: The integer array you should partition
    @param k: As description
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        # write your code here
        # you should partition the nums by k
        # and return the partition index as description
        if not nums or k is None:
            return 0
            
        left = 0
        right = len(nums) - 1
        while left < right:
            while left < right and nums[left] < k:
                left += 1
            while left < right and nums[right] >= k:
                right -= 1
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
        return left if nums[left] >= k else left + 1