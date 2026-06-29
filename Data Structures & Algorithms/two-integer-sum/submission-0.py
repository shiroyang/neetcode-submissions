class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        from collections import defaultdict
        d = defaultdict(int)
        for idx, num in enumerate(nums):
            d[num] = idx

        for idx, num in enumerate(nums):
            if target - num in d and idx != d[target-num]:
                return [idx, d[target-num]]