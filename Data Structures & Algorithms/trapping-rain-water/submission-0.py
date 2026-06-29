class Solution:
    def trap(self, height: List[int]) -> int:
        # height = [0,1,0,2,1,0,1,3,2,1,2,1]
        # LtoR   = [0,1,1,2,2,2,2,3,3,3,3,3]
        # height[::-1] = [1,2,1,2,3,1,0,1,2,0,1,0]
        # RtoL[::-1] = [1,2,2,2,3,3,3,3,3,3,3,3]
        # RtoL = [3,3,3,3,3,3,3,3,2,2,2,1]
        # min(LtoR, RtoL) = [0,1,1,2,2,2,2,3,2,2,2,1]
        # min(ltoR, RtoL) - height 
        n = len(height)
        cur_max = 0
        LR = []
        for num in height:
            cur_max = max(cur_max, num)
            LR.append(cur_max)
        cur_max = 0
        RL = []
        for num in height[::-1]:
            cur_max = max(cur_max, num)
            RL.append(cur_max)
        RL.reverse()
        ans = 0
        for i in range(n):
            ans += min(LR[i], RL[i]) - height[i]
        return ans