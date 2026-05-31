class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()

        for num in asteroids:
            if mass < num:
                return False
            
            mass += num
        
        return True