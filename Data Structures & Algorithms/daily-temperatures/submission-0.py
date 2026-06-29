class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        q = []
        n = len(temperatures)
        i = 0
        ans = [0] * n
        for i in range(n):
            cur = temperatures[i]
            while q and temperatures[q[-1]] < cur:
                prev_idx = q.pop()
                ans[prev_idx] = i - prev_idx
            q.append(i)
        return ans