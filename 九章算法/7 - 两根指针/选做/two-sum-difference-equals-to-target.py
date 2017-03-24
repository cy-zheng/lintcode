class Solution:
    """
    @param nums {int[]} n array of Integer
    @param target {int} an integer
    @return {int[]} [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum7(self, nums, target):
        # Write your code here
        data = list(enumerate(nums))
        data.sort(key=lambda x:x[1])
        diff = [0]
        for i in range(1, len(data)):
            diff.append(data[i][1] - data[i - 1][1])
        start, end = self.find_subarray(diff, target)
        return sorted([data[start][0] + 1, data[end][0] + 1])
            
    def find_subarray(self, nums, target):
        sum = 0
        cache = {}
        for i in range(len(nums)):
            sum = sum + nums[i]
            if sum in cache:
                return [cache[sum], i]
            cache[sum + target] = i
            cache[sum - target] = i