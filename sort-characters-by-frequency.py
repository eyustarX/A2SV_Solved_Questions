class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        chars = sorted(freq.items(), key=lambda x: (x[1], x[0]), reverse = True)
        ans = []

        for ch, count in chars:
            ans.append(ch * count)
        return "".join(ans)
