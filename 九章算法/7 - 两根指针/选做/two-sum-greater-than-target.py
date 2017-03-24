class Solution:
    # @param nums, an array of integer
    # @param target, an integer
    # @return an integer
    def twoSum2(self, nums, target):
        # Write your code here
        nums.sort()
        n = len(nums)
        left, right = n - 2, n - 1
        result = 0
        # two pointer jump together
        while left >= 0 and nums[left] + nums[right] > target:
            result += n - left - 1
            left -= 1
            right -= 1
        # just right pointer jump
        # start at pre loop right
        pre_right = right
        while left >= 0:
            right = pre_right
            while right < n:
                if nums[left] + nums[right] > target:
                    result += n - right
                    break
                right += 1
            if right == n:
                break
            pre_right = right
            left -= 1
            
        return result