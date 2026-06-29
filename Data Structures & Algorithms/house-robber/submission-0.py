class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp[i][flag]
        # dp[0][1] = nums[0]; dp[1][1] = nums[1]
        # dp[i][1] = dp[i-2][1]+nums[i-2]
        # dp[i][0] = max(dp[i-1][1], dp[i-2][1])

        n = len(nums)
        dp = [[0]*2 for _ in range(n)]
        dp[0][1] = nums[0]
        if n > 1: 
            dp[1][0] = nums[0]; dp[1][1] = nums[1]
        for i in range(2, n):
            dp[i][0] = max(dp[i-1][1], dp[i-2][1])
            dp[i][1] = max(dp[i-1][0], dp[i-2][1])+nums[i]
        return max(dp[-1])