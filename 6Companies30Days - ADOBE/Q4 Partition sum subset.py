# Partition sum subset

# User function Template for Python3

class Solution:
    def equalPartition(self, n, arr):
        Sum = sum(arr)
        if Sum%2 != 0:
            res = False
        else:
            Sum = int(Sum/2)
            m = [[False for x in range(Sum+1)] for y in range(n+1)]
            res = self.ss(arr,Sum,n,m)
        return res
        
    def ss(self, arr,sum,n,m):
        for j in range(sum+1): 
            m[0][j] = False
        for i in range(n+1): 
            m[i][0] = True
        for i in range(1,n+1):
            for j in range(1,sum+1):     
                if arr[i-1]<=j:
                    m[i][j] = m[i-1][j-arr[i-1]] or m[i-1][j]
                else:
                    m[i][j] = m[i-1][j]
        return m[n][sum]