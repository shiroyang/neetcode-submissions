class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        sd = list(sorted(d.items(), key=lambda x:-x[1]))
        ans = []
        for i in range(k):
            ans.append(sd[i][0])
        return ans