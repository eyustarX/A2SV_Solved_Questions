class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m,n = len(nums1), len(nums2)
        left, right = 0, m
        size = (m + n + 1) // 2

        while left <= right:
            i = left + (right - left) // 2
            j = size - i

            max_l1 = float("-inf") if i == 0 else nums1[i - 1]
            min_r1 = float("inf") if i == m else nums1[i]

            max_l2 = float("-inf") if j == 0 else nums2[j - 1]
            min_r2 = float("inf") if j == n else nums2[j]

            if max_l1 <= min_r2 and max_l2 <= min_r1:
                if (m + n) % 2 == 0:
                    return (max(max_l1, max_l2) + min(min_r1, min_r2)) / 2
                return (max(max_l1, max_l2))

            elif max_l1 > min_r2:
                right = i - 1
            else:
                left = i + 1
        

