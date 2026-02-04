class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for x in range(left,right+1):
            for s,e in ranges:
                if s<=x<=e:
                    break
            else:
                return False
        
        return True
