# ATOI ---------------------------------
class Solution:
    # your task is to complete this function
    # function should return an integer
    def atoi(self,string):
        i = 0
        res, sign = 0, 1
        if string[i] == '-':
            sign = -1
            i += 1
        for i in range(i,len(string)):
            if (ord(string[i]) - ord('0') >= 0 and ord(string[i])-ord('0') <= 9):
                res = res*10 + ord(string[i]) - ord('0')
            else:
                return -1
        return res *sign