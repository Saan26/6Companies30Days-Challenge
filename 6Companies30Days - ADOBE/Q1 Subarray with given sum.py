# Subarray with given sum ---------------------------------------------------

class Solution:
    def subArraySum(self,arr, n, s):
        cursum = 0
        l = 0
        r = 0
        while r < n:
            cursum += arr[r]
            while cursum > s:
                cursum -= arr[l]
                l += 1
            if cursum < s:
                r += 1
            if cursum == s:
                return [l+1, r+1]
        return [-1]