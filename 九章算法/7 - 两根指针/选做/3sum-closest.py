class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target : An integer
    @return : return the sum of the three integers, the sum closest target.
    """
    def threeSumClosest(self, numbers, target):
        # write your code here
        numbers.sort()
        sum = None
        for i in range(len(numbers) - 2):
            temp = numbers[i] + self.twoSumClosest(numbers[i + 1:], target - numbers[i])
            if sum is None or abs(sum - target) > abs(temp - target):
                sum = temp
        return sum

    def twoSumClosest(self, nums, target):
        # Write your code here
        result = None
        sum = None
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[right] + nums[left] == target:
                return nums[right] + nums[left]
            elif nums[right] + nums[left] > target:
                if result is None or abs(nums[right] + nums[left] - target) < result:
                    result = abs(nums[right] + nums[left] - target)
                    sum = nums[right] + nums[left]
                right -= 1
            else:
                if result is None or abs(nums[right] + nums[left] - target) < result:
                    result = abs(nums[right] + nums[left] - target)
                    sum = nums[right] + nums[left]
                left += 1
        return sum