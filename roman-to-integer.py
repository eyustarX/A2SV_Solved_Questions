class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100, "XC": 90, "L": 50, "XL": 40, "X": 10, "IX": 9, "V": 5, "IV": 4,"I": 1}
        ans=0
        i=0
        while i<len(s):
            if i+2 <= len(s) and  s[i:i+2] in {"IX", "IV", "XC", "XL", "CM", "CD"}:
                ans += roman[s[i:i+2]]
                i += 2
            else:
                ans += roman[s[i]]
                i += 1
        
        return ans
