class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)

        if n <= 1:
            return s

        half_length = n // 2
        first_half = sorted(s[:half_length])

        if n % 2 == 0:
            return "".join(first_half + first_half[::-1])
        else:
            middle_char = s[half_length]
            return "".join(first_half + [middle_char] + first_half[::-1])
