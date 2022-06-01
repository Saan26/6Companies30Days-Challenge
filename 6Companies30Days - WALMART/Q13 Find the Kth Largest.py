#  Find the Kth Largest Element 

import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k:int) -> int:
        if not nums:
            return 0

        hq = []
        for n in nums:
            heapq.heappush(hq, n)
            if k < len(hq):

                heapq.heappop(hq)
        return heapq.heappop(hq)



































