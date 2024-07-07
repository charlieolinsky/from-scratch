from TreeNode import TreeNode
 
#LrR
def inOrderTraversal(root: TreeNode):
    if root:
        inOrderTraversal(root.left)
        print(str(root.val)+' ', end='')
        inOrderTraversal(root.right)

#rLR
def preOrderTraversal(root: TreeNode):
    if root:
        print(str(root.val)+' ', end='')
        inOrderTraversal(root.left)
        inOrderTraversal(root.right)

#LRr
def postOrderTraversal(root: TreeNode):
    if root:
        inOrderTraversal(root.left)
        inOrderTraversal(root.right)
        print(str(root.val)+' ', end='')
