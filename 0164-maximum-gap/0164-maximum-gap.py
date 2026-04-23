class Solution:
    def maximumGap(self, nums):
        if len(nums) < 2:
            return 0

        min_val = min(nums)
        max_val = max(nums)

        if min_val == max_val:
            return 0

        n = len(nums)
        bucket_size = max(1, (max_val - min_val) // (n - 1))
        bucket_count = (max_val - min_val) // bucket_size + 1

        buckets = [[None, None] for _ in range(bucket_count)]

        for num in nums:
            idx = (num - min_val) // bucket_size
            b = buckets[idx]

            if b[0] is None:
                b[0] = b[1] = num
            else:
                b[0] = min(b[0], num)
                b[1] = max(b[1], num)

        max_gap = 0
        prev_max = min_val

        for b in buckets:
            if b[0] is None:
                continue
            max_gap = max(max_gap, b[0] - prev_max)
            prev_max = b[1]

        return max_gap