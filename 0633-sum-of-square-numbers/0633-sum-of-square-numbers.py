class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        k = int(c ** 0.5)
        l, r = 0, k
        while l <= r:
            y = l*l + r*r 
            if y == c:
                return True
            
            elif y < c:
                l += 1
            
            else:
                r -= 1
        
        return False