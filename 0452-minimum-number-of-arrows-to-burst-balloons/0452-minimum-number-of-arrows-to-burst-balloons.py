class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        k = len(points)
        min_value = points[0][1]
        
        for i in range(1, len(points)):
            if points[i-1][1] >= points[i][0] and min_value >= points[i][0]:
                k -= 1
            
            else:
                min_value = points[i][1]
                print(min_value)
        
        return k
