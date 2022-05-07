# Number following a pattern
class Solution:
    def printMinNumberForPattern(ob,S):
        string = ""
        i = 0
        num = 1
        if S[0] == "I":
            string += str(num)
            num += 1
        while i < len(S):
            if S[i] == "I":
                j = i
                count = 0
                while j < len(S):
                    if S[j] == "I":
                        j += 1
                        count += 1
                    else:
                        break
                for p in range(count-1):
                    string += str(num)
                    num += 1
                i = j
            elif S[i] == "D":
                j = i
                count = 0
                while j < len(S):
                    if S[j] == "D":
                        j += 1
                        count += 1
                    else:
                        break
                before = num
                num = num + count
                after = num
                while num >= before:
                    string += str(num)
                    num -= 1
                num = after+1
            i = j
        if S[-1] == "I":
            string += str(num)
        return string
