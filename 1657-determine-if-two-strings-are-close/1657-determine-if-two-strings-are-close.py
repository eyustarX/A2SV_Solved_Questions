class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        dic1 = Counter(word1)
        dic2 = Counter(word2)

        if sorted(dic1.values()) == sorted(dic2.values()) and set(dic1.keys()) == set(dic2.keys()):
            return True
        else:
            return False