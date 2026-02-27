class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        count = 0
        l = 0

        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r],0) + 1
            max_freq = max(freq.values())
            
            while (r - l + 1) - max_freq > k:
                freq[s[l]] -= 1
                l += 1
            
            count = max(count, r - l + 1)
        
        return count