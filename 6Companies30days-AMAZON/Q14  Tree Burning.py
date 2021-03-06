# Tree Burning ------------------------------------------------

class Solution:
    def minTime(self, root,target):
        
        parent, x = self.Parent(root, target)
        if x == None:
            
            return 0
        ans = 0
        burned = [x]
        q = deque()
        q.append(x)
        while len(q)>0:
            flag = False
            k = len(q)
            for i in range(k):
                curr = q.popleft()
                if curr in parent and parent[curr] not in burned:
                    burned.append(parent[curr])
                    q.append(parent[curr])
                    flag = True
                if curr.left != None and curr.left not in burned:
                    burned.append(curr.left)
                    q.append(curr.left)
                    flag = True
                if curr.right != None and curr.right not in burned:
                    burned.append(curr.right)
                    q.append(curr.right)
                    flag = True
           # print(burned)
            if flag:
                ans += 1
        return ans
        
    def Parent(self, root, target):
        p = dict()
        q = deque()
        q.append(root)
        x = None
        while len(q)>0:
            curr = q.popleft()
            if curr.data == target:
                x = curr
            if curr.left != None:
                p[curr.left] = curr
                q.append(curr.left)
            if curr.right != None:
                p[curr.right] = curr
                q.append(curr.right)
        return p, x