# Winner of an election --------------------------------------------

class Solution:
    
    def winner(self,arr,n):
        from collections import Counter
        dict = Counter(arr)
        res = []
        maxval = 0
        for k,v in dict.items():
            if v>= maxval:
                maxval = v
                
        
        for k,v in dict.items():
            # print(k,v)
            if v==maxval:
                res.append([k,v])

        res= sorted(res,key = lambda x:x[0])
    
        return res[0][0],res[0][1]