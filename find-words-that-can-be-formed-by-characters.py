from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count=0
        char=list(chars)
        char=Counter(char)

        for word in words:
            wor=Counter(list(word))
            for ch in word:
                if ch not in char or wor[ch]>char[ch]:
                    break
            else:
                count+=len(word)
        
        return count
