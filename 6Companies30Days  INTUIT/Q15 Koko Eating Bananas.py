# Koko Eating Bananas

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left,right = 1, max(piles)
        while left<right:
            mid = (left+right)//2
            required = 0
            for i in piles:
                required+=ceil(i/mid)
            if h>=required:
                right = mid
            else:
                left = mid+1
        return left
        