# Leaders in an array ---------------------------------------------------

class Solution:
    #Back-end complete function Template for Python 3
    
    #Function to find the leaders in the array.
    def leaders(self, A, N):
        stack = []
        for i in range(len(A)-1,-1,-1):
            # print(A[i])
            if len(stack)== 0:
                stack.append(A[i])
            elif A[i]>= stack[-1]:
                stack.append(A[i])
        return stack[::-1]
