class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left, right = 0, len(height) - 1

        while left < right:
            h = min(height[left],height[right])
            w = right - left
            area = h * w
            max_area = max(max_area, area)

            if height[right] < height[left]:
                right -= 1
            else:
                left += 1
        
        return max_area
            