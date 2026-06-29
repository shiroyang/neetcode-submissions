class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 入る水の量は: min(height[l], height[r]) * (r-l)
        # ans = max(min(height[l], height[r]) * (r-l))
        # two pointers, 常に bottleneck を改善する
        n = len(height)
        l = 0; r = n-1
        ans = 0
        while l < r:
            tmp = min(height[l], height[r]) * (r-l)
            ans = max(ans, tmp)
            if height[l] < height[r]: 
                l += 1
            else:
                 r -= 1
        return ans
            