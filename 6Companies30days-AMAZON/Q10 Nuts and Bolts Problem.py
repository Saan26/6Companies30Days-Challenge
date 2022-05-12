# Nuts and Bolts Problem ------------------------------------------

class Solution:

	def matchPairs(self,nuts, bolts, n):
		for i in range(n):
            e = bolts.index(nuts[i])
            bolts[i], bolts[e] = bolts[e], bolts[i]
            nuts.sort()
            bolts.sort()