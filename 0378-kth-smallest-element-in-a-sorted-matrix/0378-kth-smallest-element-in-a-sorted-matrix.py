class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        arr = []

        for row in matrix:
            arr.extend(row)
        
        heapify(arr)
        while k > 1:
            heappop(arr)
            k -= 1
        
        return arr[0]