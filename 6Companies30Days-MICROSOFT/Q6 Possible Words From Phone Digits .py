# Possible Words From Phone Digits ----------------------------------------------------------------

class Solution:
    
    #Function to find list of all words possible by pressing given numbers.
    def possibleWords(self,arr,N):
        digitstochar = {
            2 : "abc",
            3 : "def",
            4 : "ghi",
            5 : "jkl",
            6 : "mno",
            7 : "pqrs",
            8 : "tuv",
            9 : "wxyz"
        }
        res = []
        def recursive(i, curstr):
            if len(curstr) == N:
                res.append(curstr)
                return
            for c in digitstochar[arr[i]]:
                recursive(i+1, curstr + c)
        if arr:
            recursive(0,"")
        return res