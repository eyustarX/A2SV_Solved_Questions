class Solution:
    def customSortString(self, order: str, s: str) -> str:
        sub =[]

        for ch in order:
            if ch in s:
                sub.append(ch * s.count(ch))

        for i in range(len(s)):
            if s[i] not in order:
                sub.insert(i, s[i])
        
        return "".join(sub)