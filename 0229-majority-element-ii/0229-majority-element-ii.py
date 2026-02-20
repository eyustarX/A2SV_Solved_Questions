class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dic = Counter(nums)
        ans = []
        k = len(nums)//3

        for key, value in dic.items():
            if value > k:
                ans.append(key)
        
        return ans