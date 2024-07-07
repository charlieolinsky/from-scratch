class TreeNode:    
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
    #Level Order Insert (Produces a 'Complete Binary Tree')
    def insert(self, node: 'TreeNode'):        
        if not self:
            self = node
            return

        #Enqueue the root node
        q = [self]

        while q:
            cur = q.pop(0)
            
            if not cur.left:
                cur.left = node
                return
            else:
                q.append(cur.left)
                
            if not cur.right:
                cur.right = node
                return
            else:
                q.append(cur.right)
        
        