# Rotten Oranges ------------------------------------------

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q =  deque()
        visit= set()
		
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    visit.add((i, j))
                elif grid[i][j] == 2:
                    q.append((i, j))
        res = 0
        while visit and q:
			
            for _ in range(len(q)):
                i, j = q.popleft()  
                for inds in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                    if inds in visit:  
                        visit.remove(inds)
                        q.append(inds)
            res += 1
		
        return -1 if visit else res
        