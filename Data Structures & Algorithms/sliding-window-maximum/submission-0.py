class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from heapq import heapify, heappush, heappop
        h = [(-v, i) for i, v in enumerate(nums[:k])]
        heapify(h)
        ans = [-h[0][0]]

        for r in range(k, len(nums)):
            heappush(h, (-nums[r], r))
            l = r - k
            while h[0][1] <= l:
                heappop(h)
            ans.append(-h[0][0])
        
        return ans
                