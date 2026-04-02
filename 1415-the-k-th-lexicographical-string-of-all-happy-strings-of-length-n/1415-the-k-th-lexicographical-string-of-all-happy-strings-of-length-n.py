class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        ans = []
        happy = "abc"

        def backtracking(i, path):
            if i == n:
                ans.append("".join(path))
                return
            
            for j in range(3):
                if not path or path[-1] != happy[j]:
                    path.append(happy[j])
                    backtracking(i + 1, path)
                    path.pop()
        
        backtracking(0,[])

        return ans[k-1] if k - 1 < len(ans) else ""