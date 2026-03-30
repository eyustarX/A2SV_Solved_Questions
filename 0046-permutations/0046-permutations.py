class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        perm = []
        used = [False] * len(nums)

        def backtracking():
            if len(perm) == len(nums):
                ans.append(perm[:])
                return
            
            for i in range(len(nums)):
                if not used[i]:
                    perm.append(nums[i])
                    used[i] = True

                    backtracking()

                    perm.pop()
                    used[i] = False
        
        backtracking()
        return ans