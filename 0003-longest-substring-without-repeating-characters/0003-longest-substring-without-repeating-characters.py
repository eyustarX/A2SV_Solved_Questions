class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = set()
        max_len = 0
        left = 0

        for i, ch in enumerate(s):
            while ch in substring:
                substring.remove(s[left])
                left += 1
            
            substring.add(ch)
            max_len = max(max_len, i - left + 1)

        return max_len