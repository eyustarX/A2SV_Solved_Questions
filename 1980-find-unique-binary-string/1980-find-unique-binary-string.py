class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        arr = []
        
        for i in range(len(nums)):
            if nums[i][i] == "1":
                arr.append("0")
            
            else:
                arr.append('1')
        
        return "".join(arr)