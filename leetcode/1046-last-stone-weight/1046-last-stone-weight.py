class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        def heapdown(arr,i):
            left = 2 * i + 1
            right = 2 * i + 2
            largest = i
            n = len(arr)

            if left < n and arr[largest] < arr[left]:
                largest = left
            if right < n and arr[largest] < arr[right]:
                largest = right
            
            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                heapdown(arr, largest)
            
        for i in range(len(stones) // 2 - 1, -1, -1):
            heapdown(stones, i)
        
        size = len(stones)
        
        while size > 1:
            stones[0], stones[-1] = stones[-1], stones[0]
            max1 = stones.pop()
            size -= 1

            if not stones:
                break
            
            heapdown(stones,0)
            stones[0], stones[-1] = stones[-1], stones[0]
            max2 = stones.pop()
            size -= 1
            
            if max1 != max2:
                k = abs(max1 - max2)
                stones.append(k)
                size += 1

            heapdown(stones, 0)
        
        return stones[0] if stones else 0