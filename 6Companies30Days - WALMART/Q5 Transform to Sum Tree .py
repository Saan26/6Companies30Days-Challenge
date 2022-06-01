# Transform to Sum Tree 

class Solution:
    def toSumTree(self, root) :
        self.solve(root)
    def solve(self,node):
        if node:
            val = node.data
            node.data = self.solve(node.left) + self.solve(node.right)
            return node.data + val
        return 0