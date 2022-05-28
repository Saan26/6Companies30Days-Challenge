# Number of Boomerangs

class Solution:
    def numberOfBoomerangs(self, p: List[List[int]]) -> int:
        length, t = len(p), 0
        D = [[0]*length for i in range(length)]
        for i in range(length):
        	dict_ = {}
        	for j in range(length):
        		if j > i: D[i][j] = D[j][i] = (p[j][0]-p[i][0])**2 + (p[j][1]-p[i][1])**2
        		dict_[D[i][j]] = dict_[D[i][j]] + 1 if D[i][j] in dict_ else 1
        	t += sum(r*(r-1) for r in dict_.values())
        return t