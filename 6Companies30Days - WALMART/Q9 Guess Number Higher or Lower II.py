# Guess Number Higher or Lower II

class Solution:
    def getMoneyAmount(self, n: int) -> int:
        
        @functools.cache
        def pay_to_guess(low, high):
            
            if high - low == 1:
                return low
        
            if low == high:
                return 0
            
            min_ = float('inf')
            for i in range(low+1, high):
                lower = i + pay_to_guess(low, i-1)
                higher = i + pay_to_guess(i+1, high)
                min_ = min(min_, max(lower, higher))
            
            return min_
        
        return pay_to_guess(1, n)
        