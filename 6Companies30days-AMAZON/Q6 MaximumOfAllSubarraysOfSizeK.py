# Maximum of all subarrays of size k

class Solution:
    
    #Function to find maximum of each subarray of size k.
    def max_of_subarrays(self,nums,n,k):
    	output = []
	    l = r = 0
	    q = deque()
	    while r < len(nums):
		    while q and nums[q[-1]] < nums[r]:
			    q.pop()
		    q.append(r)
		
		    if l > q[0]:
			    q.popleft()		
		    if r + 1 >= k:
			    output.append(nums[q[0]])
			    l += 1
		    r += 1
	    return output

