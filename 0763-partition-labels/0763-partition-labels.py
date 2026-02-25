class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic = defaultdict()
        for i, ch in enumerate(s):
            dic[ch] = i
        
        partition = []
        start, end = 0, 0

        for i, ch in enumerate(s):
            end = max(end, dic[ch])

            if i == end:
                partition.append(end - start + 1)
                start = i + 1
        
        return partition