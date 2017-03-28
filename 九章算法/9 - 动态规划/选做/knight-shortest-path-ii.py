import sys
class Solution:
    # @param {boolean[][]} grid a chessboard included 0 and 1
    # @return {int} the shortest path
    def shortestPath2(self, grid):
        # Write your code here
        if not grid or not grid[0]:
            return -1
            
        m, n = len(grid), len(grid[0])
        distance = [[-1 for i in range(n)] for j in range(m)]
        distance[0][0] = 0
        step_x = [-1, 1, -2, 2]
        step_y = [-2, -2, -1, -1]
        
        for j in range(1, n):
            for i in range(m):
                if grid[i][j] == 1:
                    continue
                small_d = self.get_small_distance(distance, i, j, step_x, step_y)
                distance[i][j] = small_d
      
        return distance[m - 1][n - 1]
        
    def get_small_distance(self, distance, i, j, step_x, step_y):
        m, n = len(distance), len(distance[0])
        min_d = sys.maxint
        for _ in range(4):
            x = i + step_x[_]
            y = j + step_y[_]
            if (x >= 0 and y >= 0) and (x < m and y < m) and distance[x][y] != -1:
                min_d = min(min_d, distance[x][y] + 1)
                
        return -1 if min_d == sys.maxint else min_d
        
        