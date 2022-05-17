#Stickler Thief -----------------------------------

class Solution:  
    
    #Function to find the maximum money the thief can get.
    def FindMaxSum(self,a, n):
        dp = [-1 for _ in range(n+1)]
        def recur(ind):
            if ind >= n:
                return 0
            if dp[ind] != -1:
                return dp[ind]
            pick = a[ind] + recur(ind+2)
            notpick = recur(ind+1)
            dp[ind] =  max(pick,notpick)
            return dp[ind]
        return recur(0)
            
