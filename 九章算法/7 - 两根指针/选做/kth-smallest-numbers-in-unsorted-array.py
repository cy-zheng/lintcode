import sys
class Solution:
    # @param {int} k an integer
    # @param {int[]} nums an integer array
    # return {int} kth smallest element
    def kthSmallest(self, k, nums):
        # Write your code here
        if not k or not nums:
            return
        
        return self.quick_select(k, nums, 0, len(nums) - 1)
        
    def quick_select(self, k, nums, start, end):
        if start == end:
            return nums[start]
            
        i, j = start, end
        pivot = nums[(start + end) / 2]
        
        while i <= j:
            while i <= j and nums[i] < pivot:
                i += 1
            while i <= j and nums[j] > pivot:
                j -= 1
                
            if i <= j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
                
        if start + k - 1 <= j:
            return self.quick_select(k, nums, start, j)
        if start + k - 1 >= i:
            return self.quick_select(k - (i - start), nums, i, end)
            
        return nums[j + 1]
                
        