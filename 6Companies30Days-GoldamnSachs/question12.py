# No of Squares in N*N chessboard


class Solution:
    def squaresInChessBoard(self, n):
        ans = 0
        while n:
            ans += n * n
            n -= 1
        return ans