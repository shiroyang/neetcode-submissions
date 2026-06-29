class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import deque, Counter
        d1 = Counter()
        d2 = Counter(t)
        q = deque()
        ans = ""
        for idx, c in enumerate(s):
            is_ok = True
            d1[c] += 1
            q.append(c)
            for key, val in d2.items():
                if d1.get(key, 0) < val:
                    is_ok = False; break
            if not is_ok: continue

            if ans == "" or len(ans) > len(q):
                ans = ''.join(q)

            while q and d1[q[0]] > d2[q[0]]:
                d1[q.popleft()] -= 1

            if ans == "" or len(ans) > len(q):
                ans = ''.join(q)       
        
        return ans

            