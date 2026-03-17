class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7
        
        def p(a, b, mod):
            if b == 0:
                return 1
            
            value = p(a, b // 2, mod)
            
            if b % 2 == 0:
                return (value * value) % mod
            else:
                return (a * value * value) % mod
        
        k = n // 2

        if n % 2 == 0:
            return (p(5, k, mod) * p(4, k, mod)) % mod
        else:
            return (p(5, k + 1, mod) * p(4, k, mod)) % mod