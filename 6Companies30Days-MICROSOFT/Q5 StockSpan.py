# Stock Span --------------------------------

class Solution:
    
    #Function to calculate the span of stockâ€™s price for all n days.
    def calculateSpan(self,arr,n):
        stack, lst = [], []
        for i in range(n):
            while (len(stack) != 0 and arr[stack[-1]] <= arr[i]):
                stack.pop()
            if len(stack) == 0:
                lst.append(i+1)
            else:
                lst.append(i - stack[-1])
            stack.append(i)
        return lst