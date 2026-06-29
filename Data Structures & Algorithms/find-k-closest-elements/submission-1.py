class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        from heapq import heapify, heappush, heappop
        
        h = []
        for item in arr:
            delta = item - x
            if delta < 0:
                delta = -delta - 0.1
            h.append(delta)
        print(h)
        heapify(h)

        ans = []

        for _ in range(k):
            delta = heappop(h)
            if delta == int(delta):
                ans.append(x+delta)
            else:
                ans.append(round(x-delta-0.1))
        
        return sorted(ans)


