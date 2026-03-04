class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix = [0] * (len(s))
        for shift in shifts:
            if shift[2] == 0:
                prefix[shift[0]] -= 1
                if shift[1] + 1 < len(s): 
                    prefix[shift[1] + 1] += 1
            else:
                prefix[shift[0]] += 1 
                if shift[1] + 1 < len(s):
                    prefix[shift[1] + 1] -= 1
       
        ans = []
        for i in range(len(s)):
            if i != 0:
                prefix[i] += prefix[i-1]

            new_char = (ord(s[i]) - ord('a') + prefix[i]) % 26
            ans.append(chr(ord('a') + new_char))
        
        return "".join(ans)