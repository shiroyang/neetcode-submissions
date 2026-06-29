class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def is_ok(x):
            tmp = 0
            for pile in piles:
                tmp += (pile + x - 1) // x
            return tmp <= h
        
        l = 0; r = 10 ** 10
        while r - l > 1:
            mid = (r+l) >> 1
            if is_ok(mid):
                r = mid
            else:
                l = mid
        return r
