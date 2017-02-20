class Solution:
    """
    @param nums: A list of integers.
    @return: A list of unique permutations.
    """
    def permuteUnique(self, nums):
        # write your code here
        results = []
        if nums is None:
            return results
        nums.sort()
        self.dfsHelper(nums[:], [], results, nums)
        return results

    def dfsHelper(self, nums, subset, results, S):
        if len(subset) == len(S):
            results.append(subset[:])
            return
        for i in range(len(nums)):
            if nums.count(nums[i]) > 1 and nums.index(nums[i]) != i:
                continue
            subset.append(nums[i])
            self.dfsHelper(nums[:i] + nums[i + 1:], subset, results, S)
            subset.pop()
