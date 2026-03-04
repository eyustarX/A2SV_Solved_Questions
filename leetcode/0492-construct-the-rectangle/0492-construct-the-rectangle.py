class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        k = int(area ** 0.5) + 1
        
        if k * k == area:
            return [k,k]

        freq = {area: 1}
        n,m= float('inf'), 0
        for i in range(1,k):
            j = area % i
            if j  == 0:
                freq[area // i] = i
        print(freq)
        for key in freq:
            if key - freq[key] < n - m:
                n= key
                m= freq[key]
        
        return [n,m]