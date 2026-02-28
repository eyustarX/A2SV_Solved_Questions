class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            left, right = 0, len(word) - 1
            flag = True
            while left < right:
                if word[left] != word[right]:
                    flag = False
                    break
                left += 1
                right -= 1
            
            if flag:
                return word
        
        return ""