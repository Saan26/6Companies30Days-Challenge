# Column name from a given column number--------------------

class Solution:
    def colName (self, n):
        result = ""
        while n > 0:
            c = chr(ord('A') + (n-1) % 26)
            result = c + result
            n = (n-1)//26
        
        return result