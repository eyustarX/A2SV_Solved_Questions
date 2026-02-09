class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic=Counter(nums)
        s=dict(sorted(dic.items(),key=lambda x:x[1],reverse=True))
        ans=[]
        
        for key in s:
            if k>0:
                ans.append(key)
                k-=1
            else:
                break
        
        return ans

       
