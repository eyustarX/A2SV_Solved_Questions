class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            s = 0
            while n>0:
                num = n % 10
                s += pow(num, 2)
                n //= 10
            
            n = s
            if n in seen:
                return False
            seen.add(n)
        
        return True
