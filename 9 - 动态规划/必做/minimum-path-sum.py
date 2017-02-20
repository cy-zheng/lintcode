class Solution:
    """
    @param grid: a list of lists of integers.
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def minPathSum(self, grid):
        # write your code here
        m = len(grid)
        n = len(grid[0])
        cache = [[None for i in range(n)] for j in range(m)]
        cache[0][0] = grid[0][0]
        for i in range(1, m):
            cache[i][0] = cache[i - 1][0] + grid[i][0]
        for j in range(1, n):
            cache[0][j] = cache[0][j - 1] + grid[0][j]
            
        for i in range(1, m):
            for j in range(1, n):
                cache[i][j] = min(cache[i - 1][j], cache[i][j - 1]) + grid[i][j]
        
        return cache[m - 1][n - 1]
            