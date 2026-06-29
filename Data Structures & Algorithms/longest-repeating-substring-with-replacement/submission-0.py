class Solution:
    from collections import defaultdict
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0
        d = defaultdict(int)
        ans = 0
        max_f = 0
        for r in range(len(s)):
            d[s[r]] += 1
            max_f = max(d.values())
            while (r-l+1) - max_f > k:
                d[s[l]] -= 1
                max_f = max(d.values())
                l += 1
            ans = max(ans, r-l+1)
        return ans


            