class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def s(maximum):
            count = 1
            value = 0
            i = 0
            while i < len(weights):
                if value + weights[i] <= maximum:
                    value += weights[i]
                else:
                    value = weights[i]
                    count += 1
                i += 1
                if count > days:
                    break
            return count <= days    
        
        left = max(weights)
        right = sum(weights)

        while left <= right:
            mid = (left + right) // 2
            if s(mid):
                right = mid -1
            else:
                left = mid + 1
        
        return left
        
        