# Brackets in MCM ------------------------------------

class Solution:
    def __init__(self):
        self.charname ='A'
        self.ans = []
    def printMatrix(self,i,j,bracket):
        if i == j:
            self.ans.append(self.charname)
            i = ord(self.charname[0])
            i += 1
            self.charname = chr(i)

        else:
            self.ans.append('(')
            self.printMatrix(i,bracket[i][j],bracket)
            self.printMatrix(bracket[i][j] + 1 ,j,bracket)

            self.ans.append(')')
            
        return  ''.join(self.ans)
    
    def matrixChainOrder(self, arr, n):
        
        n = n-1
        dp = [[0 for i in range(n)] for i in range(n)]
        bracket = [[0 for i in range(n)] for i in range(n)]
        
        ans = []
        for g in range(n):
            i = 0
            j = g
            while i<n and j<n:
                if g == 0:
                    dp[i][j] = 0
                elif g == 1:
                    dp[i][j] = arr[i]*arr[j]*arr[j+1]

                else:
                    mi = 111111111
                    for k in range(i,j):
                        lc = dp[i][k]
                        rc = dp[k+1][j]
                        tm = arr[i]*arr[k+1]*arr[j+1]
                        mc = tm+lc+rc
                        if mc<mi:
                            mi = mc
                            
                    bracket[i][j] = k
                    dp[i][j]= mi

                i+=1
                j+=1
                
        return self.printMatrix(0,n-1,bracket)



