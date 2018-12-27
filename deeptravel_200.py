class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        """深度优先遍历。grid[i][j] 为1就遍历其上下左右。若其上下左右为1再继续遍历
        """
        if grid is None:
            return 0
        count = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == 1:
                    self.numIslands_core(i, j, grid)
                    count += 1
        return count

    def numIslands_core(self, i, j, grid):
        if i < 0 or j < 0 or i > len(grid)-1 or j > len(grid[0])-1 or grid[i][j] != 1:
            return
        grid[i][j] = 'label'
        self.numIslands_core(i-1, j, grid)
        self.numIslands_core(i, j-1, grid)
        self.numIslands_core(i, j+1, grid)
        self.numIslands_core(i+1, j, grid)