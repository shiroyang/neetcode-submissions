class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find peak
        from bisect import bisect_left
        n = len(nums)
        if nums[0] <= nums[-1]:
            idx = bisect_left(nums, target)
            return idx if idx < n and nums[idx] == target else -1
        l = 0; r = n - 1
        mid = -1
        while r - l > 0:
            mid = (l+r) // 2
            if nums[mid] > nums[mid+1]:
                break
            elif nums[mid] > nums[0]:
                l = mid
            else:
                r = mid
        
        if target < nums[0]:
            # find right
            l = mid+1; r = n-1
        else:
            #find left  
            l = 0; r = mid
        while r - l >= 0:
            mid = (l+r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else: r = mid - 1
        return -1