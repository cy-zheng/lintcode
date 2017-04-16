class Solution:
    # @param {int[]} stones a list of stones' positions in sorted ascending order
    # @return {boolean} true if the frog is able to cross the river or false
    def canCross(self, stones):
        # Write your code here
        dp = {}
        for stone in stones:
            dp[stone] = set()
        dp[stones[0]].add(0)
        for i in range(len(stones) - 1):
            for item in dp[stones[i]]:
                if item - 1 != 0 and stones[i] + item - 1 in dp:
                    dp[stones[i] + item - 1].add(item - 1)
                if stones[i] + item in dp:
                    dp[stones[i] + item].add(item)
                if stones[i] + item + 1 in dp:
                    dp[stones[i] + item + 1].add(item + 1)
                        
        return len(dp[stones[-1]]) != 0