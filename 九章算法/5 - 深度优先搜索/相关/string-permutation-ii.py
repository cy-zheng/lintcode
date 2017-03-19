class Solution:
    # @param {string} str a string
    # @return {string[]} all permutations
    def stringPermutation2(self, str):
        # Write your code here
        results = []
        if not str:
            return ['']
        slist = list(str)
        slist.sort()
        self.dfsHelper(slist[:], [], results, str)
        return results

    def dfsHelper(self, nums, subset, results, S):
        if len(subset) == len(S):
            results.append(''.join(subset))
            return
        for i in range(len(nums)):
            if nums.count(nums[i]) > 1 and nums.index(nums[i]) != i:
                continue
            subset.append(nums[i])
            self.dfsHelper(nums[:i] + nums[i + 1:], subset, results, S)
            subset.pop()
