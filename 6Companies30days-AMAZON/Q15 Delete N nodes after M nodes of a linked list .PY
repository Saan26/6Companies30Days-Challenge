#Delete N nodes after M nodes of a linked list  --------------------------------

class Solution:
    def skipMdeleteN(self, head, M, N):
        start = head
        lis1 = []
        while start:
            lis1.append(start)
            start = start.next
        length = len(lis1)
        
        lis2 = []
        count = 0
        i = 0
        while i < length:
            if count < M:
                lis2.append(lis1[i])
                count += 1
                i += 1
            else:
                count = 0
                i += N
        length2 = len(lis2)
        q = lis2[0]
        head = q
        for i in range(1, length2):
            hh = lis2[i]
            q.next = hh
            q = q.next
        q.next = None
        return head