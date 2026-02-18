class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for i in range(len(heights)):
            
            swap = False
            for j in range(len(heights) - i - 1):
                if heights[j] < heights[j + 1]:
                    heights[j], heights[j + 1] = heights[j + 1], heights[j]
                    names[j], names[j + 1] = names[j + 1], names[j]
                    swap = True
            
            if not swap:
                break

        return names