# Minimum swaps to arrange a binary grid 

class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        zero, n = [], len(grid)
        for row in grid:
            tmp = 0
            while row and row.pop() == 0:
                tmp += 1
            zero.append(tmp)

        res = 0
        for i in range(n):
            
            if zero[i] >= n-i-1:
                continue

            for j in range(i+1, n):
                if zero[j] >= n-i-1:
                    break
            if zero[j] < n-i-1:
                return -1
            zero[i+1:j+1] = zero[i:j]
            res += j-i
        return res