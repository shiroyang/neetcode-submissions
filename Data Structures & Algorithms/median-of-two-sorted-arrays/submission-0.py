from bisect import bisect_left, bisect_right
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)

        def find_target(k: int) -> int:
            # k: 1-indexed
            if m == 0:
                return nums2[k - 1]
            if n == 0:
                return nums1[k - 1]

            # nums1 側で候補探索
            l1, r1 = 0, m - 1
            while l1 <= r1:
                mid = (l1 + r1) // 2
                x = nums1[mid]

                lt = mid + bisect_left(nums2, x)          # < x の個数
                le = (mid + 1) + bisect_right(nums2, x)   # <= x の個数
                L, R = lt + 1, le

                if L <= k <= R:
                    return x
                elif k < L:
                    r1 = mid - 1
                else:
                    l1 = mid + 1

            # nums2 側で候補探索
            l2, r2 = 0, n - 1
            while l2 <= r2:
                mid = (l2 + r2) // 2
                x = nums2[mid]

                lt = mid + bisect_left(nums1, x)
                le = (mid + 1) + bisect_right(nums1, x)
                L, R = lt + 1, le

                if L <= k <= R:
                    return x
                elif k < L:
                    r2 = mid - 1
                else:
                    l2 = mid + 1

            # ここに来るのは基本的に「入力がソートされてない」等
            raise ValueError("not found: check input sortedness")

        total = m + n
        if total % 2 == 1:
            return float(find_target(total // 2 + 1))
        else:
            return (find_target(total // 2) + find_target(total // 2 + 1)) / 2.0
