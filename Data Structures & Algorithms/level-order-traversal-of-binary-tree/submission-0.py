# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        if not root: return []
        q = deque([(root, 1)])
        ans = []
        while q:
            x, depth = q.popleft()
            if len(ans) < depth:
                ans.append([])
            ans[-1].append(x.val)
            if x.left: q.append((x.left, depth+1))
            if x.right: q.append((x.right, depth+1))
        
        return ans