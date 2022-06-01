# Number of Unique Paths

class Solution:
    #Function to find total number of unique paths.
    def NumberOfPaths(self,a, b):
        dp = [[1 for i in range(b)]for j in range(a)]
        
        for i in range(1,a):
            for j in range(1,b):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
                
        return dp[a-1][b-1]