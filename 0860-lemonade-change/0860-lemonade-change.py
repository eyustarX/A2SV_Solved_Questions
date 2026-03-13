class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        freq = defaultdict(int)

        for bill in bills:
            freq[bill] += 1
            k = bill - 5

            tw = k // 20
            if tw > 0 and 20 in freq:
                n = min(tw, freq[20])
                k -= (20 * n)
                freq[20] -= n
            
            ten = k // 10
            if ten > 0 and 10 in freq:
                n = min(ten, freq[10])
                k -= (10 * n)
                freq[10] -= n
            
            fi = k // 5
            if fi > 0 and 5 in freq:
                n = min(fi, freq[5])
                k -= (5 * n)
                freq[5] -= n
            
            if k > 0:
                return False
        
        return True