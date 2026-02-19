class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        k = len(arr)
        result = []

        while k > 1:
            max_no = 0

            for i in range(k):
                max_no = max(arr[i],max_no)

            idx = arr.index(max_no)
            if idx == k - 1:
                k -= 1
                continue
            
            if idx != 0:
                flip = arr[:idx + 1]
                flip.reverse()

                for i in range(len(flip)):
                    arr[i] = flip[i]
                result.append(idx + 1)

            flip = arr[:k]
            flip.reverse()

            for i in range(len(flip)):
                arr[i] = flip[i]
            result.append(k)

            k -= 1
        
        return result