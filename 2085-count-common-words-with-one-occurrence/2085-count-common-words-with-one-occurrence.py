class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        dic1 = Counter(words1)
        dic2 = Counter(words2)
        count = 0

        for key in dic1:
            if key in dic2:
                if dic1[key] == 1 and dic2[key] == 1:
                    count += 1
        
        return count