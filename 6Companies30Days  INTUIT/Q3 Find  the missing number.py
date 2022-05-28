# Find the missing number 

import math
max_ = 6
def getVal(Str, i, m):
   
    if(i + m > len(Str)):
        return -1
    val = 0
    for j in range(m):
        ch = (ord(Str[i + j]) -
             ord('0'))
        if(ch < 0 or ch > 9):
            return -1
        val = val * 10 + ch
    return val

def missingNumber(Str):

    for m in range(1, max_ + 1):
 
        n = getVal(Str, 0, m)
        if(n == -1):
            break

        missingNo = -1
        fail = False
        i = m
        while(i != len(Str)):
            if((missingNo == -1) and
               (getVal(Str, i, 1 +
                int(math.log10(n + 2))) ==
                               n + 2)):
                missingNo = n + 1
                n += 2
 
            elif((getVal(Str, i, 1 +
                  int(math.log10(n + 1))) ==
                                 n + 1)):
                n += 1
            else:
                fail = True
                break
            i += 1 + int(math.log10(n))
 
        if(not fail):
            return missingNo
           

    return -1