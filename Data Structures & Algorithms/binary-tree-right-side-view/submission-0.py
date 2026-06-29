# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        from collections import deque

        q = deque([(root, 1)])
        ans = []

        while q:
            x, depth = q.popleft()
            if len(ans) < depth:
                ans.append([])
            ans[-1].append(x.val)
            if x.left: q.append((x.left, depth+1))
            if x.right: q.append((x.right, depth+1))
        
        res = []
        for i in range(len(ans)):
            res.append(ans[i][-1])

        return res