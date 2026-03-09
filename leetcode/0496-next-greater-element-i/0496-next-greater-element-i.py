class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        my_dict = {}

        for num in nums2:
            while stack and stack[-1] < num:
                k = stack.pop()
                my_dict[k] = num
            
            stack.append(num)
        
        for num in stack:
            my_dict[num] = -1

        ans = []

        for num in nums1:
            ans.append(my_dict[num])

        return ans
