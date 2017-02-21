class Solution:
    # @param {int} n a positive integer
    # @return {int} an integer
    _dp = [0]
    def numSquares(self, n):
        # Write your code here
        dp = self._dp
        while len(dp) <= n:
            dp += min(dp[-i*i] for i in range(1, int(len(dp)**0.5+1))) + 1,
        return dp[n]