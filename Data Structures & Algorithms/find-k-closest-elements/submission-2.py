class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        from heapq import heapify, heappush, heappop
        
        h = []
        for item in arr:
            h.append((abs(item-x), item))
        heapify(h)

        ans = []
        for _ in range(k):
            ans.append(heappop(h)[1])
        
        return sorted(ans)


