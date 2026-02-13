class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        ps = {}
        sp = {}
        word =s.split()

        if len(pattern) != len(word):
            return False
        
        for ch, w in zip(pattern,word):
            if ch in ps and ps[ch] != w:
                return False
            
            if w in sp and sp[w] != ch:
                return False
            
            ps[ch] = w
            sp[w] = ch
        
        return True
        
        



         