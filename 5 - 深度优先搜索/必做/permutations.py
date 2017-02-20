class Solution:
    """
    @param nums: A list of Integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        # write your code here
        results = []
        if nums is None:
            return results
        nums.sort()
        self.dfsHelper(nums[:], [], results, len(nums))
        return results

    def dfsHelper(self, nums, subset, results, length):
        if len(subset) == length:
            results.append(subset[:])
            return
        for i in range(len(nums)):
            subset.append(nums[i])
            self.dfsHelper(nums[:i] + nums[i + 1:], subset, results, length)
            subset.pop()
