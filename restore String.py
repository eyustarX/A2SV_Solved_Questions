class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans=[0 for _ in range(len(s))]
        for i,ch in enumerate(s):
            ans[indices[i]]=ch
        
        return "".join(ans)
