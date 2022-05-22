# Express as sum of power of natural numbers ----------------------------------------------------------

#User function Template for python3
class Solution:
	def check(self,num,restnum,curr,n,ans=0):
            if restnum==0:
                ans+=1
                
            r = int(num**(1/n))
            for i in range(curr+1,r+1):
                temp = restnum - int(i**n)
                if temp>=0:
                    ans+= self.check(num,temp,i,n,0)
            return ans
            
    def numOfWays(self, n, x):
        t1 = self.check(n,n,0,x,0)
        return t1%1000000007
        
