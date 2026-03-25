class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        comb = []
        def backtrack(start):
            if len(comb) == k:
                ans.append(comb[:])
                return 
            
            for i in range(start, n + 1):
                comb.append(i)
                backtrack(i + 1)
                comb.pop()
        
        backtrack(1)
        return ans