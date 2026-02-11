class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 != 0:
            return []

        count = Counter(changed)
        ans = []
        if count[0] % 2 != 0:
            return []

        for _ in range(count[0] // 2):
            ans.append(0)
        count[0] = 0

        for x in sorted(count):
            if x == 0:
                continue

            if count[x] > count[2 * x]:
                return []

            for _ in range(count[x]):
                ans.append(x)
                count[2 * x] -= 1

        return ans
