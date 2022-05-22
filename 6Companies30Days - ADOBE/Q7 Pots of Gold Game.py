# Pots of Gold Game-----------------------------------------------------------

class Solution:
    def maxCoins(self,arr, n):
        mat = [[0 for i in range(n+1)] for i in range(n+1)]
        return self.fun(mat,arr,0,n-1)
        
    def fun(self,mat,arr,l,r):

        if l>r:
            return 0
        if mat[l][r] != 0: return mat[l][r]
        if l<=r and l<len(arr) and r>=0:
            t1 = arr[l] + min(self.fun(mat,arr,l+2,r), self.fun(mat,arr,l+1,r-1))
            t2 = arr[r]+ min(self.fun(mat,arr,l+1,r-1),self.fun(mat,arr,l,r-2))
            mat[l][r] = max(t1,t2)
            return mat[l][r] 
        mat[l][r] = 0
        return 0    