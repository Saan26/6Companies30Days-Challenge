# Unit Area of largest region of 1's  -------------------------------

class Solution:

    #Function to find unit area of the largest region of 1s.
	def findMaxArea(self, grid):
		rows, cols = len(grid), len(grid[0])
        visit = set()
        area = 0
        
        def dfs(r,c):
            if (r<0 or r == rows or c<0 or c == cols or (r,c) in visit or grid[r][c]==0):
                return 0
            if grid[r][c]:
                visit.add((r,c))
                return (1 + dfs(r+1,c) +dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)+dfs(r-1,c-1)+dfs(r+1,c+1)+dfs(r+1,c-1)+dfs(r-1,c+1))
        
        for r in range(rows):
            for c in range(cols):
                area = max(area, dfs(r,c))
        return area
