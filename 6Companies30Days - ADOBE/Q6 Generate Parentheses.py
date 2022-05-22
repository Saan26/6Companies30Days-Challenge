# Generate Parentheses ----------------------------------------------------------

class Solution:
    def isValid(self,n,open,close,lis,ans):
        if close>open or open>n or close>n: 
            return 
        if open == close == n:
            ans.append(lis)
            return 
        temp = lis+ '('
        self.isValid(n,open+1,close,temp,ans)
        
        temp1 = lis+')'
        self.isValid(n,open,close+1,temp1,ans)
        
    def AllParenthesis(self,n):
        ans = []
        self.isValid(n,0,0,'',ans)
        return ans