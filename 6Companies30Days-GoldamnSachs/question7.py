# Distributing N items for S size circle starting at Kth position ------------------------
# s -> Size of circle
# n -> Number of items
# k -> Initial position
def lastItem(s, n, k):
	if (n <= s - k + 1):
	    return n + k - 1    
	n = n - (s - k + 1)
	if(n % s == 0):
		return n
	else:
		return n % s
s = 5
n = 10
k = 3
print(lastItem(s, n, k))

