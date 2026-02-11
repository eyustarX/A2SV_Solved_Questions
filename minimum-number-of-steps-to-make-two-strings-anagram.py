class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_dict = Counter(s)
        t_dict = Counter(t)
        count = 0

        for ch in s_dict:
            if s_dict[ch] > t_dict[ch]:
                count += (s_dict[ch] - t_dict[ch])
                t_dict[ch] = s_dict[ch]
        
        for key, value in s_dict.items():
            if key not in t_dict:
                count += value

        return count
