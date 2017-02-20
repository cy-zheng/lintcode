class Solution:
    # @param {int[][]} grid a 2D grid
    # @return {int} an integer
    def shortestDistance(self, grid):
        # Write your code here
        # 判断当前节点是不是没走过的empty节点
        def isVaild(grid, r, c, row, col, visited):
            if r >= 0 and r < row and c >= 0 and c < col \
                    and grid[r][c] == 0 and (not visited[r][c]):
                return True            
            return False 
            
        row = len(grid)
        if row == 0:
            return 0
        col = len(grid[0])
        nbrow = [1, -1, 0, 0]
        nbcol = [0, 0, 1, -1]
        empty, wall, house, distance = self.initialize(grid, row, col)
        for h in house: #对于每个房子BFS
            jump = -1 
            queue = [h]
            # visited distance等辅助数组，要使用最原始的数组
            # （每个元素对应一个格子，存各种数据，而不是存格子下标）
            # （不要用in查询，增加复杂度）
            visited = [[False for c in range(col)] for r in range(row)]
            while queue:
                jump += 1
                size = len(queue)
                for s in range(size):
                    node = queue.pop(0)
                    if grid[node[0]][node[1]] == 0:
                        distance[node[0]][node[1]] += jump
                    for i in range(4):
                        nx = node[0] + nbrow[i]
                        ny = node[1] + nbcol[i]
                        if isVaild(grid, nx, ny, row, col, visited):
                            visited[nx][ny] = True
                            queue.append((nx, ny))
            for i in range(row):
                for j in range(col):
                    if not visited[i][j]:
                        # 假如当前empty，存在一个房子无法到达
                        # 那么以后邮局不可能选在它上面，路径也不能通过它
                        # 标记为墙，以后不需要探测
                        grid[i][j] = 2
                        distance[i][j] = 99999
        result = min([min(l) for l in distance])
        return result if result != 99999 else -1
             
    def initialize(self, grid, row, col):
        empty = []
        wall = []
        house = []
        distance = [[0 for c in range(col)] for r in range(row)]
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    house.append((r, c))
                elif grid[r][c] == 2:
                    wall.append((r, c))
                else:
                    empty.append((r, c))
        for r, c in wall:
            distance[r][c] = 99999
        for r, c in house:
            distance[r][c] = 99999  
        return empty, wall, house, distance