# Smallest range in K lists

#User function Template for python3
import heapq
class Solution:
    def smallestRange(self, KSortedArray, n, k):
        # code here
        # print the smallest range in a new line
        minheap=[]
        maxi=-float('inf')
        for i in range(k):
            heapq.heappush(minheap,(numbers[i][0],i,0))
            maxi=max(numbers[i][0],maxi)
        heapq.heapify(minheap)
        difference=maxi-minheap[0][0]
        ans=[minheap[0][0],maxi]
       
        while True:
            mini,r,c=heapq.heappop(minheap)
            if difference>maxi-mini:
                difference=maxi-mini
                ans=[mini,maxi]
            if c+1>=len(numbers[r]):
                break
            num=numbers[r][c+1]
            maxi=max(maxi,num)
            heapq.heappush(minheap,(num,r,c+1))
        return ans