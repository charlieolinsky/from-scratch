from TreeNode import *
from traverse import *
from search import *

# Create Tree
root = TreeNode(5)
root.insert(TreeNode(3))
root.insert(TreeNode(7))
root.insert(TreeNode(6))
root.insert(TreeNode(8))

# In, Pre, Post Order Traversals
print("In-Order Traversal:")
inOrderTraversal(root)
print("\n-------------------")

print("Pre-Order Traversal:")
preOrderTraversal(root)
print("\n-------------------")

print("Post-Order Traversal:")
postOrderTraversal(root)
print("\n-------------------")

# DFS
print("DFS (Recursive) for value 8 found:", recursive_dfs(root, 8))
print("-------------------")
print("DFS (Iterative) for value 8 found:", iterative_dfs(root, 8))