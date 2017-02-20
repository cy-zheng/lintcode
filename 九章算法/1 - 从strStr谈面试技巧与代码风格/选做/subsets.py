class Solution:
    """
    @param S: The set of numbers.
    @return: A list of lists. See example.
    """
    def subsets(self, S):
        # write your code here
        results = []
        if not S:
            return results
        S.sort()
        self.dfsHelper(S, 0, [], results)
        return results

    def dfsHelper(self, S, startnum, subset, results):
        results.append(subset[:])
        for i in range(startnum, len(S)):
            subset.append(S[i])
            self.dfsHelper(S, i + 1, subset, results)
            subset.pop()