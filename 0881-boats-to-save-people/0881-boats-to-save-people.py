class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        ans = 0
        left, right = 0, len(people) - 1

        while left <= right:
            if people[right] == limit:
                ans += 1
                right -= 1
            
            elif people[right] + people[left] > limit:
                ans += 1
                right -= 1
            
            elif people[right] + people[left] <= limit:
                ans += 1
                left += 1
                right -= 1
            
        return ans
        