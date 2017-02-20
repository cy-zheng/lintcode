class Solution:
    # @param {boolean[][]} grid a boolean 2D matrix
    # @return {int} an integer
    def numIslands(self, grid):
        # Write your code here
        self.row = len(grid)
        if self.row == 0:
            return 0
        self.col = len(grid[0])
        
        self.visited = [[False for i in range(self.col)] for j in range(self.row)]
        count = 0
        for r in range(self.row):
            for c in range(self.col):
                if self.check(grid, r, c):
                    self.bfs(grid, r, c)
                    count += 1
        return count
        
    def check(self, grid, r, c):
        if r >= 0 and r < self.row and c >= 0 and c < self.col \
            and grid[r][c] and (not self.visited[r][c]):
            return True
        return False
        
    def bfs(self, grid, r, c):
        nbrow = [1, -1, 0, 0]
        nbcol = [0, 0, 1, -1]
        queue = [(r, c)]
        while queue:
            (x, y) = queue.pop(0)
            self.visited[x][y] = True
            for i in range(4):
                nx = x + nbrow[i]
                ny = y + nbcol[i]
                if self.check(grid, nx, ny):
                    queue.append((nx, ny))
                