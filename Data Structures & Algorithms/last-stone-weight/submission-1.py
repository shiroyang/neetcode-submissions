class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = []
        for num in stones: h.append(-num)
        heapq.heapify(h)
        while len(h) > 1:
            l = -heapq.heappop(h)
            r = -heapq.heappop(h)
            heapq.heappush(h, -abs(l-r))
        return -h[0]