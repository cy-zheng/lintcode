class Solution:
    """
    @param n and m: positive integer(1 <= n , m <= 100)
    @return an integer
    """ 
    def uniquePaths(self, m, n):
        # write your code here
        cache = [[None for i in range(n)] for j in range(m)]
        for i in range(m):
            cache[i][0] = 1
        for j in range(n):
            cache[0][j] = 1
            
        for i in range(1, m):
            for j in range(1, n):
                cache[i][j] = cache[i - 1][j] + cache[i][j - 1]
                
        return cache[m - 1][n - 1]
            