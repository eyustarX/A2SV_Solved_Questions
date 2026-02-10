class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        dic={'even':0,'odd':0}
        for num in nums:
            if num%2==0:
                dic['even']+=num
            else:
                dic['odd']+=num
        ans=[]
        for i in queries:

            k=nums[i[1]]
            nums[i[1]]+=i[0]
            if nums[i[1]]%2==0 and k%2!=0:
                dic['even']+=nums[i[1]]
            elif k%2==0 and nums[i[1]]%2==0:
                dic['even']+=i[0]
            elif nums[i[1]]%2!=0 and k%2==0:
                dic['even']-=k
            ans.append(dic['even'])

        return ans
