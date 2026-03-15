class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        freq = Counter(answers)
        ans = 0

        for key, value in freq.items():
            rabbit = key + 1
            group = (key + value) // rabbit
            ans += group * rabbit

        return ans