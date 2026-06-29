class Solution:
    def search(self, nums: List[int], target: int) -> int:
        from bisect import bisect_left
        idx = bisect_left(nums, target)
        return idx if idx < len(nums) and nums[idx] == target else -1