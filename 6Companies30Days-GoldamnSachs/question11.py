# Missing and Repeating Number -----------------------------------

class Solution:
    def findTwoElement( self,arr, n): 
        ans = []
        Sum = n*(n+1)//2
        sumOfSquares = (n*(n+1)*(2*n+1))//6
        missing = repeating = 0
        for i in range(n):
            Sum -= arr[i]
            sumOfSquares -= arr[i] * arr[i]
        missing =(Sum + sumOfSquares//Sum)//2
        repeating = missing - Sum
        ans.append(repeating)
        ans.append(missing)
        return ans
