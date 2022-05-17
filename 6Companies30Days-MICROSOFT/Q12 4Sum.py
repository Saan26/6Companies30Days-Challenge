# 4 SUM -------------------------------

class Solution:
    def fourSum(self, arr, target):
        arr.sort()
        res, quad = [], []
        def helper(k,start, target):
            if k != 2:
                for i in range(start, len(arr)-k+1):
                    if i > start and arr[i] == arr[i-1]:
                        continue
                    quad.append(arr[i])
                    helper(k-1,i+1, target-arr[i])
                    quad.pop()
                return
            l, r = start, len(arr)-1
            while l <r:
                if arr[l] + arr[r] < target:
                    l += 1
                elif arr[l] + arr[r] > target:
                    r -= 1
                else:
                    res.append(quad+[arr[l],arr[r]])
                    l += 1
                    while l < r and arr[l] == arr[l-1]:
                        l += 1
        helper(4,0,target)
        return res