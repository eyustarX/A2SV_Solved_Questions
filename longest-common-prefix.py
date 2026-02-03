class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        short=min(strs, key=len)
        for i in range(len(short)):
            for word in strs:
                if word[i]!=short[i]:
                    return short[:i]
        return short
        
