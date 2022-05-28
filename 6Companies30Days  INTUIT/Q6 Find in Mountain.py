# Find in Mountain

# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def peakIndexInMountainArray(self, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()
        left = 0
        right = n - 1
        while left <= right:
            mid = left + (right - left) // 2
            midVal = mountainArr.get(mid)
            if (mid == 0 or midVal > mountainArr.get(mid-1)) and (mid == n-1 or midVal > mountainArr.get(mid+1)):
                return mid
            elif mid == 0 or midVal > mountainArr.get(mid-1):
                left = mid + 1
            else:
                right = mid - 1
        return -1
    
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()
        peak = self.peakIndexInMountainArray(mountainArr)
        
        def binarySearchInIncreasingArr(left, right):
            ans = -1
            while left <= right:
                mid = left + (right - left) // 2
                midVal = mountainArr.get(mid)
                if midVal == target:
                    return mid
                if midVal > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1
        
        def binarySearchInDecreasingArr(left, right):
            ans = -1
            while left <= right:
                mid = left + (right - left) // 2
                midVal = mountainArr.get(mid)
                if midVal == target:
                    return mid
                if midVal > target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1
        
        res = binarySearchInIncreasingArr(0, peak)
        if res != -1: return res
        return binarySearchInDecreasingArr(peak+1, n-1)