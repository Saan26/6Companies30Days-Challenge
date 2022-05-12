# Phone Directory -----------------------------------

class Solution:
    def displayContacts(self, n, contact, s):
        contact=set(contact)
        ans=[]
        for i in range(len(s)):
            search = s[0:i+1]
            equal = [e for e in contact if e.startswith(search)]
            equal.sort()
            if len(equal)==0:
                ans.append([0])
            else:
                ans.append(equal)
        return ans