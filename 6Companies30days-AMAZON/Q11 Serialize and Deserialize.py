# Tree Serialization and Deserialization --------------------------------------------

class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None            
class Code:
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        def doit(node):
            if node:
                vals.append(str(node.val))
                doit(node.left)
                doit(node.right)
            else:
                vals.append('#')
                return
        vals = []
        doit(root)
        return ' '.join(vals)
    def deserialize(self,data):
        def dfs():
            val = next(vals)
            if val == "#":
                return None
            
            root = TreeNode(int(val))
            root.left = dfs()
            root.right = dfs()
            return root
        vals =  iter(data.split() )  
        return dfs()