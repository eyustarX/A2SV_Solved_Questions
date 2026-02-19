class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        ans = 0
        k = 0
        
        for i in range(len(piles)//3):
            ans += piles[-2 + k]
            k -= 2
        
        return ans