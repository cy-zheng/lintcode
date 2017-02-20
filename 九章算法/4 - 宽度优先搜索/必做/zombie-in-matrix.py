class Solution:
    # @param {int[][]} grid  a 2D integer grid
    # @return {int} an integer
    def zombie(self, grid):
        # Write your code here
        row = len(grid)
        if row == 0:
            return 0
        col = len(grid[0])
        
        jump = -1
        nbrow = [1, -1, 0, 0]
        nbcol = [0, 0, 1, -1]
        queue = []
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    queue.append((r,c))
        while queue:
            size = len(queue)
            jump += 1
            for s in range(size):
                (x, y) = queue.pop(0)
                for i in range(4):
                    nx = x + nbrow[i]
                    ny = y + nbcol[i]
                    if nx >= 0 and nx < row and ny >= 0 and ny < col \
                        and grid[nx][ny] == 0 and ((nx, ny) not in queue):
                        #最后一个条件非常重要，重复元素不入队
                        grid[nx][ny] = 1
                        queue.append((nx, ny))
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 0:
                    return -1               
        return jump