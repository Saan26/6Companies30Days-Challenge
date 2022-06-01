# Power Of Numbers 

class Solution:
    #Complete this function
    def power(self,N,R):
        m = 1000000007
        if R ==0:
            return 1
        if R == 1:
            return N
        ans = self.power(N, R/2)
        if R%2 == 0:
            return ans%m*ans%m
        else:
            return N%m*ans%m*ans%m