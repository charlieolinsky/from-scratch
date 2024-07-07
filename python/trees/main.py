from TreeNode import *
from traverse import *

#Create Tree
root = TreeNode(5)
root.insert(TreeNode(3))
root.insert(TreeNode(7))
root.insert(TreeNode(6))
root.insert(TreeNode(8))

# In, Pre, Post Order Traversals
inOrderTraversal(root)
print('\n')
preOrderTraversal(root)
print('\n')
postOrderTraversal(root)    