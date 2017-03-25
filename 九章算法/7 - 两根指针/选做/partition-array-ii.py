class Solution:
    # @param {int[]} nums an integer array
    # @param {int} low an integer
    # @param {int} high an integer
    # @return nothing
    def partition2(self, nums, low, high):
        # Write your code here
        i, j = 0, len(nums) - 1
        flag = True
        while i <= j and flag:
            flag = False
            while i <= j and nums[i] < low:
                i += 1
            if i <= j:
                pointer = i + 1
                while pointer <= j:
                    if nums[pointer] < low:
                        nums[i], nums[pointer] = nums[pointer], nums[i]
                        flag = True
                        break
                    pointer += 1
                
            while i <= j and nums[j] > high:
                j -= 1
            if i <= j:
                pointer = j - 1
                while pointer >= i:
                    if nums[pointer] > high:
                        nums[j], nums[pointer] = nums[pointer], nums[j]
                        flag = True
                        break
                    pointer -= 1
                