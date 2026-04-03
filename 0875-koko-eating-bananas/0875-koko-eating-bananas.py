class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        
        def check(mid):
            count = 0
            for num in piles:
                count += (num + mid - 1) // mid

                if count > h:
                    return count
                
            return count
        
        while left <= right:
            mid = left + (right - left) // 2
            if check(mid) <= h:
               right = mid - 1
            else:

                left = mid + 1
        
        return left