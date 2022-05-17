# Count Number of SubTrees having given Sum -----------------------------------------\

'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

def countSubtreesWithSumX(root, x):
    treecount = [0]
    helper(treecount, root,x)
    return treecount[0]
def helper(count, root, x):
    if not root:
        return 0
    if root:
        left = helper(count,root.left,x)
        right = helper(count, root.right,x)
        total = root.data + left + right
        if total== x:
            count[0] += 1
        return total