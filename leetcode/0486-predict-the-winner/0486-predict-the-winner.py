class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        def back(l, r):
            if l == r:
                return nums[l]

            left = nums[l] - back(l + 1, r)
            right = nums[r] - back(l, r - 1)

            return max(left, right)
            
        return back(0, n-1)>=0



