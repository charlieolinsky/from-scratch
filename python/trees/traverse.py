import python.trees.TreeNode as TreeNode
 
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

#Create Tree
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)

# In, Pre, Post Order Traversals
inOrderTraversal(root)
print('\n')
preOrderTraversal(root)
print('\n')
postOrderTraversal(root)    