class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        def back(l, r):
            length = r - l +1
            me = 0 
            him = 0
            if l == r:
                if n %2 == 0:
                    him += nums[l]
                    return -him
                else:
                    me+=nums[l]
                    return me
            

            if length % 2 ==1:
            
                if n%2 == 1:
                    return max(nums[l] + back(l+1, r), nums[r] + back(l, r-1))
                else:
                    return min(-nums[l]+back(l+1, r), -nums[r] + back(l, r-1))
            else:

                if n%2 == 0:
                    return max(nums[l] + back(l+1, r), nums[r] + back(l, r-1))
                else :
                    return min(-nums[l]+back(l+1, r), -nums[r] + back(l, r-1))
        return back(0, n-1)>=0





        # p1 = 0
        # p2 = 0

        # while nums:
        #     if len(nums) > 1 and nums[-2] > nums[-1]:
        #         p1 += nums[0]
        #         nums.pop()
            
        #     else:
        #         p1 += nums[-1]
        #         nums.pop()
        #     if not nums:
        #         break

        #     if nums[0] > nums[-1]:
        #         p2 += nums[0]
        #         nums.pop(0)
        #     else:
        #         p2 += nums[-1]
        #         nums.pop()
        
        # print(p1, p2)   
        # return p1 > p2