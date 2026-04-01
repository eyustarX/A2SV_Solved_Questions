class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtracking(start, path):
            if len(path) > 1:
                ans.append(path[:])
            
            used = set()

            for i in range(start, len(nums)):
                if nums[i] in used:
                    continue
                
                if not path or nums[i] >= path[-1]:
                    used.add(nums[i])
                    path.append(nums[i])

                    backtracking(i + 1, path)
                    path.pop()
            
        backtracking(0, [])

        return list(ans)