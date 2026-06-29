class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = set(nums)
        ans = 0
        for num in d:
            if (num - 1) in d: continue
            length = 1
            while (num + length) in d:
                length += 1
            ans = max(ans, length)
        return ans
