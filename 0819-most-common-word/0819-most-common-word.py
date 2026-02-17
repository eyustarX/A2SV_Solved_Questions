class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned = set(banned)

        word = ""
        words = []

        for ch in paragraph.lower():
            if ch.isalnum():
                word += ch
            else:
                if word:
                    words.append(word)
                    word = ""
        if word:
            words.append(word)

        freq = Counter(words)

        for w, x in freq.most_common():
            if w not in banned:
                return w