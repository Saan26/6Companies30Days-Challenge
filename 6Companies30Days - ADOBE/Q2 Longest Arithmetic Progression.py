# Longest Arithmetic Progression ------------------------------------------------

class Solution:
    def lengthOfLongestAP(self, A, n):
        from collections import defaultdict
        dp = defaultdict(lambda: 1)
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                dp[j, A[j]-A[i]] = dp[i, A[j]-A[i]] + 1
        return max(dp.values())