class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left, right = 0, len(skill) - 1
        ans = 0
        k = (skill[left]  + skill[right])

        while left < right:
            if skill[left]  + skill[right] != k:
                return -1
                
            ans += (skill[left] * skill[right])
            left += 1
            right -= 1
        
        return ans