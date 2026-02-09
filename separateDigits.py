class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        n="".join(map(str,nums))
        return [int(i) for i in n]
