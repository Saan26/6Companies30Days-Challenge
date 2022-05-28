# Partition a set into two subsets such that the difference of subset sums is minimum

import sys
def ss(arr,sum,n,m):
    vec = []
    mn = sys.maxsize
    for j in range(sum+1): 
        m[0][j] = False
    for i in range(n+1): 
        m[i][0] = True
    for i in range(1,n+1):
        for j in range(1,sum+1):    
            if arr[i-1]<=j:
                m[i][j] = m[i-1][j  -arr[i-1]] or m[i-1][j]
            else:
                m[i][j] = m[i-1][j]
    for i in range(n+1):
        for j in range((sum+2)//2): 
            if i==n and m[i][j] == True:
                vec.append(j)  
    for i in range(len(vec)):
        mn = min(mn,sum-2*vec[i])
    return mn

def main():
    arr = [1,2,7]
    ran = sum(arr)
    n = len(arr)
    m = [[False for x in range(ran+1)] for y in range(n+1)]
    res = ss(arr,ran,n,m)
    print(res)
main()