class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        left, right = 1, position[-1] - position[0]

        def distance(length):
            count = 1
            last = position[0]

            for i in range(1, len(position)):
                if position[i] - last >= length:
                    count += 1
                    last = position[i]
                
                if count == m:
                    return True

        while left <= right:
            mid = left + (right - left) // 2

            if distance(mid):
                left = mid + 1
            else:
                right = mid - 1
        
        return right