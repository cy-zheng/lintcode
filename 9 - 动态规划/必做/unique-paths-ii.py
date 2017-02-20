class Solution:
    """
    @param obstacleGrid: An list of lists of integers
    @return: An integer
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        # write your code here
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        cache = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                break
            cache[i][0] = 1
        for j in range(n):
            if obstacleGrid[0][j] == 1:
                break
            cache[0][j] = 1
            
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    continue
                cache[i][j] = cache[i - 1][j] + cache[i][j - 1]
                
        return cache[m - 1][n - 1]