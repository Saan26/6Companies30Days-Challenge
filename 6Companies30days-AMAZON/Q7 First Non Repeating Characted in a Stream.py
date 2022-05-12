# Fisrt non repeating character in a stream ----------------------------

class Solution:
	def FirstNonRepeating(self, A):
	    freq = [0]*26
	    lis = ""
	    q = []
	    for i in range(len(A)):
	        
	        ch = A[i]
	        freq[ord(ch)-97] += 1
	        if freq[ord(ch)-97] == 1:
	            q.append(ch)
	        else:
	            while q and freq[ord(q[0])-97] > 1:
	                q.pop(0)
	        if q:
	            lis += q[0]
	        else:
	            lis += "#"
	    return lis
	        