# Valid Suduko --------------------------------------------

class Solution:
    
    def isValid(self, mat):
        from collections import defaultdict
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                if mat[r][c] == 0:
                    continue
                if(mat[r][c] in rows[r] or mat[r][c] in cols[c] or mat[r][c] in squares[(r//3,c//3)]):
                    return 0
                cols[c].add(mat[r][c])
                rows[r].add(mat[r][c])
                squares[(r//3,c//3)].add(mat[r][c])
        return 1