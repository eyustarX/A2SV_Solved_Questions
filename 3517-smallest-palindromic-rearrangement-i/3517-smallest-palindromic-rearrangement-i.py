class Solution:
    def smallestPalindrome(self, s: str) -> str:
        if len(s)<=1:
            return s
        
        if len(s) % 2 == 0:
            word = s[:len(s)//2]
            word = sorted(word)
            return "".join(word + word[::-1])

        
        else:
            word = s[:len(s)//2]
            word = sorted(word)
            w = word[::-1]
            word.append(s[len(s)//2])
            return "".join(word + w)
