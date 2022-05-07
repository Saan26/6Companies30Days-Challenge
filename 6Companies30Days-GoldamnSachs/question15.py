# Array Pair sum divisibility 
class Solution:
	def canPair(self, nuns, k):
	    
        if(len(nuns)==0 or len(nuns)==1):
            return 0
        dic = {}
        for i in range(len(nuns)):
            if(((nuns[i] % k) + k) % k in dic):
                dic[((nuns[i] % k) + k) % k]+=1
            else:
                dic[((nuns[i] % k) + k) % k]=1
        for x in dic:
            if(x==0):
                if(dic[x]%2!=0):
                    return 0
            elif(2*x==k):
                if(dic[x]%2!=0):
                    return 0
            else:
                if((k-x) in dic):
                    if(dic[x]!=dic[k-x]):
                        return 0
                else:
                    return 0
        return 1