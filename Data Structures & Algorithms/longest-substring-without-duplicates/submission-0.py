class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        win = deque()
        d = set()
        ans = 0
        for c in s:
            while win and c in d:
                l = win.popleft()
                d.remove(l)
            win.append(c)
            d.add(c)
            ans = max(ans, len(win))
        ans = max(ans, len(win))
        return ans
            