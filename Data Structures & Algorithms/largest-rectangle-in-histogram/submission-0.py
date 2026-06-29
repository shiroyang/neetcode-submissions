class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # monotonic stack
        # store index
        # [4, 5, 6, 4] when reaching last 4, 5 and 6 stops growing
        # [0, 1, 2, 3]
        heights.append(0)
        stack = []
        ans = 0
        for idx, cur in enumerate(heights):
            while stack and heights[stack[-1]] > cur:
                h = heights[stack.pop()]
                w = idx if not stack else idx - stack[-1] - 1
                ans = max(ans, h*w)
            stack.append(idx)
        return ans
