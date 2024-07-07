from TreeNode import TreeNode

def recursive_dfs(root: TreeNode, target: int) -> bool:
    if not root:
        return False
    if root.val == target:
        return True
    return recursive_dfs(root.left, target) or recursive_dfs(root.right, target) 


def iterative_dfs(root: TreeNode, target: int) -> bool:
    if not root:
        return False
    
    stack = [root]
    while stack:
        cur = stack.pop()
        
        if cur.val == target:
            return True
         
        if cur.right:
            stack.append(cur.right)
        if cur.left:
            stack.append(cur.left)
    
    return False     
        

