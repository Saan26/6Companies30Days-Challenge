# Number of Provinces

class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        
        if not M: return 0
        s = len(M)
        seen = set()
        cnt = 0
        for i in range(s):
            if i not in seen:
                q = [i]
                while q:
                    p = q.pop(0)
                    if p not in seen:
                        seen.add(p)
                        q += [k for k,adj in enumerate(M[p]) if adj and (k not in seen)]
                cnt += 1
        
        return cnt