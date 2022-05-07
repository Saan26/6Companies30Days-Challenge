# Total Decode ways

class Solution:
	def CountWays(self, str):
		dp ={len(str) : 1}
		
		def dfs(i):
		    if i in dp:
		        return dp[i]
		    if str[i] == '0':
		        return 0
		    res = dfs(i+1)
		    if((i + 1) < len(str) and (str[i] == '1' or str[i] == '2' and str[i+1] in '0123456')):
		        res += dfs(i+2)
		    dp[i] = res
		    return res
		    
	    return dfs(0)
