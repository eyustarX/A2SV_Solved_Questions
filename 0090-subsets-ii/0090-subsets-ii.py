class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        sub = []
        seen = set()

        def subset(i):
            if i == len(nums):
                t = tuple(sub)
                if t not in seen:
                    ans.append(sub[:])
                    seen.add(t)
                return
            
            sub.append(nums[i])
            subset(i + 1)

            sub.pop()
            subset(i + 1)
        
        subset(0)
        return ans