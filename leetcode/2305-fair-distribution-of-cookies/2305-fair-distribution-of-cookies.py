class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        distribute = [0] * k
        ans = float('inf')

        def backtrack(index):
            nonlocal ans

            if index == len(cookies):
                ans = min(ans, max(distribute)) 
                return 
            
            for i in range(k):
                distribute[i] += cookies[index]

                backtrack(index + 1)

                distribute[i] -= cookies[index]

                if distribute[i] == 0:
                    break
        
        backtrack(0)

        return ans