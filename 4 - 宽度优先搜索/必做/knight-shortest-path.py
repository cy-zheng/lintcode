# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    # @param {boolean[][]} grid a chessboard included 0 (False) and 1 (True)
    # @param {Point} source a point
    # @param {Point} destination a point
    # @return {int} the shortest path 
    def shortestPath(self, grid, source, destination):
        # Write your code here
        row = len(grid)
        if row == 0:
            return 0
        col = len(grid[0])
        
        jump = -1
        visited = [[False for i in range(col)] for j in range(row)]
        nbrow = [1, -1, 2, 2, 1, -1, -2, -2]
        nbcol = [2, 2, 1, -1, -2, -2, 1, -1]
        queue = [(source.x, source.y)]
        while queue:
            size = len(queue)
            jump += 1
            for s in range(size):
                (x, y) = queue.pop(0)
                if (x, y) == (destination.x, destination.y):
                    return jump
                visited[x][y] = True
                for i in range(8):
                    nx = x + nbrow[i]
                    ny = y + nbcol[i]
                    if nx >= 0 and nx < row and ny >= 0 and ny < col \
                        and (not grid[nx][ny]) and (not visited[nx][ny]) \
                        and ((nx, ny) not in queue): #最后一个条件非常重要，重复元素不入队
                        queue.append((nx, ny))
        return -1
        
        
        