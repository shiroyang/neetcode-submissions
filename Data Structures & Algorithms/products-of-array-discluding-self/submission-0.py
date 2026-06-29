class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # l = [1, 1, 2, 6, 24]
        l = [1]
        for num in nums: l.append(l[-1]*num)
        l.pop()

        # r = [1, 4, 12, 24, 24]
        r = [1]
        for num in nums[::-1]: r.append(r[-1]*num)
        r.pop()

        # ans = [1*24, 1*12, 2*4, 6*1]
        ans = [l[i]*r[len(l)-i-1] for i in range(len(l))]
        return ans