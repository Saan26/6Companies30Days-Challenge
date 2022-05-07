# Count the subarrays having product less than k----------- 

class Solution:
    def countSubArrayProductLessThanK(self, a, n, k):
        start = end = res = 0
        p =1
        for end in range(len(a)):
            p *= a[end]
            while start < end and p >= k:
                p /= a[start]
                start += 1
            if p < k:
                res += (end - start) +1
                
        return res