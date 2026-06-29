class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        c = set()
        for item in nums:
            if item not in c:
                c.add(item)
            else:
                return True
        return False