# count ways to reach Nth staircase-----------------------------

class Solution:
    
    #Function to count number of ways to reach the nth stair 
    #when order does not matter.
    def countWays(self,m):
        if(m%2==0):
            return m//2+1
        else:
            
            return (m+1)//2