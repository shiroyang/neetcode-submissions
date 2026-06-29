# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        def find_depth(cur, depth):
            if not cur: return depth
            return max(find_depth(cur.left, depth+1), find_depth(cur.right, depth+1))

        return find_depth(root, 0)