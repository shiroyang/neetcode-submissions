class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # two pointers でやるのがこつ
        # まず i を決めてします。そして、j, k をtwo pointers ではめる
        # pruning: while nums[i] == nums[i-1]: i += 1;
        # pruning: while nums[j] == nums[j-1]: j += 1
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]: continue
            j = i+1
            k = n-1
            while j < k:
                tmp = nums[i] + nums[j] + nums[k]
                if tmp > 0:
                    k -= 1
                elif tmp < 0:
                    j += 1
                else:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < n and nums[j] == nums[j-1]:
                        j += 1

        return ans