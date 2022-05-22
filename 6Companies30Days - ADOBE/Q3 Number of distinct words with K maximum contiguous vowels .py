# Number of distinct words with K maximum contiguous vowels  ----------------------------------------

class Solution:
    def kvowelwords(self, N,K):
        i, j = 0, 0
        MOD = 1000000007
        dp = [[0 for i in range(K + 1)]for i in range(N + 1)]
        sum = 1
        def power(a, b, p):
            res = 1
            a = a % p
            if (a == 0):
                return 0
            while (b > 0):
                if (b & 1):
                    res = (res * x) % p
                b = b >> 1
                a = (a * a) % p
         
            return res
        
        for i in range(1, N + 1):
            dp[i][0] = sum * 21
            dp[i][0] %= MOD
            sum = dp[i][0]
            for j in range(1, K + 1):
                if (j > i):
                    dp[i][j] = 0
                elif (j == i):
                    dp[i][j] = power(5, i, MOD)
                else:
                    dp[i][j] = dp[i - 1][j - 1] * 5
                dp[i][j] %= MOD
                sum += dp[i][j]
                sum %= MOD
 
        return sum