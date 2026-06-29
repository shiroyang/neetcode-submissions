class Solution:
    def findMin(self, nums: List[int]) -> int:
        # [3,4,5,1,2], find the peak
        # a[i] > a[i+1]
        l = 0; r = len(nums) - 1
        if nums[0] <= nums[-1]: return nums[0]
        while r - l > 0:
            mid = (l+r) // 2
            if nums[mid+1] < nums[mid]:
                return nums[mid+1]
            elif nums[mid] > nums[0]:
                l = mid
            else:
                r = mid