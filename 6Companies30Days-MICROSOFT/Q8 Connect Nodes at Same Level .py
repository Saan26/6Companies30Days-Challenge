# Connect Nodes at Same Level -----------------------------------------------

class Solution:
    #Function to connect nodes at same level.
    def connect(self, root):
        if not root:
            return None        
        head =  root
        
        while head:

            dummy = Node(0)
            temp = dummy

            while head:
                if head.left:
                    temp.nextRight = head.left
                    temp =  temp.nextRight
                if head.right:
                    temp.nextRight = head.right
                    temp = temp.nextRight
                head = head.nextRight

            head = dummy.nextRight
        return root