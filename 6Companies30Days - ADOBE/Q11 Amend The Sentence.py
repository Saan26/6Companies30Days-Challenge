# Amend The Sentence --------------------------------------------------------------

import re
class Solution:
    def amendSentence(self, s):
        ans = ''

        for i in range(len(s)):
            if s[i].isupper():
                if len(ans)==0:
                    ans += s[i].lower()
                else:
                    ans+= ' '
                    ans += s[i].lower()
                
            else:
                ans += s[i]
                
        return ans