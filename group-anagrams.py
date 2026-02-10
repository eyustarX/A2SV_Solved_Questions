class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for ch in strs:
            c=tuple(sorted(ch))
            dic[c].append(ch)
        
        return list(dic.values())
