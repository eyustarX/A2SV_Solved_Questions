class Solution:
    def myPow(self, x: float, n: int) -> float:
        def p(a, b):
            if b == 0:
                return 1
            
            value = p(a, b // 2)
            
            if b % 2 == 0:
                return value * value
            else:
                return a * value * value
        
        if n < 0:
            return 1 / p(x, -n)
        
        return p(x, n)