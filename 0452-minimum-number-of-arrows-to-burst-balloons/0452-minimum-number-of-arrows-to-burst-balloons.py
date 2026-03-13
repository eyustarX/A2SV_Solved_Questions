class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        ans = 1
        min_value = points[0][1]

        for i in range(1, len(points)):
            if min_value < points[i][0]:
                ans += 1
                min_value = points[i][1]
        
        return ans