class Solution:
    # @param {int} m the number of eggs
    # @param {int} n the umber of floors
    # @return {int} the number of drops in the worst case
    def dropEggs2(self, m, n):
        # Write your code here
        # Solution: http://datagenetics.com/blog/july22012/index.html
        dp = [[0] * (n + 1) for _ in xrange(m + 1)]
        
        for i in xrange(1, m + 1):
            dp[i][1] = 1
            dp[i][0] = 0

        for i in xrange(1, n + 1):
            dp[1][i] = i

        import sys
        for i in xrange(2, m + 1):
            for j in xrange(2, n + 1):
                dp[i][j] = sys.maxint
                for k in xrange(1, j + 1):
                    '''
                    If we drop an egg from floor n, one of two events happens:

                    1) The egg breaks, so now our problem is reduced to a tower of height n-1, and we now have e-1 eggs.
                    
                    2) The egg doesn't break and now we need to check k-n floors and we still have e eggs.
                    '''
                    # if i == 2:
                    #     print j, k, dp[i - 1][k - 1], dp[i][j - k]
                    dp[i][j] = min(dp[i][j], \
                        1 + max(dp[i - 1][k - 1], dp[i][j - k]))

        return dp[m][n]