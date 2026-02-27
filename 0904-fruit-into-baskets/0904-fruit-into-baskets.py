class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        hash_map = defaultdict(int)
        left = 0
        max_fruits = 0

        for i, num in enumerate(fruits):
            hash_map[num] += 1

            while len(hash_map) > 2:
                hash_map[fruits[left]] -= 1

                if hash_map[fruits[left]] == 0:
                    del hash_map[fruits[left]]
                left += 1

            max_fruits = max(max_fruits, i - left + 1)
        
        return max_fruits
            
                