# Find Array Given Subset Sums

class Solution:
    def recoverArray(self, n: int, sums: List[int]) -> List[int]:
        result = []
        sums.sort()
        for _ in range(n): 
            difference = sums[1] - sums[0]
            s0, s1 = [], []
            dict_ = defaultdict(int)
            ifYes = False 
            for i, x in enumerate(sums): 
                if not dict_[x]: 
                    s0.append(x)
                    dict_[x+difference] += 1
                    if x == 0: ifYes = True 
                else: 
                    s1.append(x)
                    dict_[x] -= 1
            if ifYes: 
                result.append(difference)
                sums = s0 
            else: 
                result.append(-difference)
                sums = s1
        return result 