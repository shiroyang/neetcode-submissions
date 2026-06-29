class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        from collections import deque
        q = deque()
        s = 0
        res = 10**32
        for num in nums:
            s += num
            q.append(num)
            while s >= target:
                res = min(res, len(q))
                s -= q.popleft()
            
        return 0 if res == 10**32 else res