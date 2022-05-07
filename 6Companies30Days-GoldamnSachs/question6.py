# Greatest Common Divisor Of Strings -----------------------
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if not (str1 + str2 == str2 + str1):
            return  ""
        if str1 == str2 :
            return str1
        (str1, str2) = (str1, str2) if len(str1) < len(str2) else (str2,str1)
        if str1 == str2[:len(str1)]:
            return self.gcdOfStrings(str2[len(str1):],str1)
        return ''