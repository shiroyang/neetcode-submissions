class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter, deque
        d1 = Counter(s1)
        d2 = Counter()
        q = deque()
        l = 0
        for c in s2:
            q.append(c)
            d2[c] += 1
            if d1 == d2: 
                return True
            while d2[c] > d1.get(c, 0) and q:
                d2[q.popleft()] -= 1
        return False


