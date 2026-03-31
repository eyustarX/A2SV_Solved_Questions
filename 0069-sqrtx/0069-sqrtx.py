class Solution:
    def mySqrt(self, x: int) -> int: 
        def sqrt(left, right):
            if left > right:
                return right
                
            mid = (left + right) // 2

            if mid * mid == x:
                return mid
            elif mid * mid > x:
                return sqrt(left, mid - 1)
            else:
                return sqrt(mid + 1, right)
        
        return sqrt(0, x)