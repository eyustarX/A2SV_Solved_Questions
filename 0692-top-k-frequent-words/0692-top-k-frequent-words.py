class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)

        heap = [(-value,key) for key, value in count.items()]
        heapify(heap)
        ans = []
        for _ in range(k):
            res = heappop(heap)[1]
            ans.append(res)
        
        return ans