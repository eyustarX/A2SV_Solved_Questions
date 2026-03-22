class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        left = 0
        right = len(s) - 1
        vowel = ['a','e','i','o','u']

        while left < right:
            if s[left].lower() in vowel and s[right].lower() in vowel:
                s[left],s[right] = s[right],s[left]
                left += 1
                right -= 1
            
            if s[left].lower() not in vowel:
                left += 1
            
            if s[right].lower() not in vowel:
                right -= 1
        
        return "".join(s)