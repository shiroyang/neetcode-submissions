# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        is_ok = True

        def dfs(x):
            if not x:
                return 0
            l = dfs(x.left) 
            r = dfs(x.right)
            nonlocal is_ok
            if abs(l-r) > 1: is_ok = False
            return max(l, r) + 1

        dfs(root)
        return is_ok