# IPL Match Day 2 ----------------------------------------------------------------

class Solution:
    def max_of_subarrays(self,arr,n,k):
        from collections import deque
        output = []
	    l = r = 0
	    q = deque()
	    while r < len(arr):
		    while q and arr[q[-1]] < arr[r]:
			    q.pop()
		    q.append(r)
		
		    if l > q[0]:
			    q.popleft()		
		    if r + 1 >= k:
			    output.append(arr[q[0]])
			    l += 1
		    r += 1
	    return output