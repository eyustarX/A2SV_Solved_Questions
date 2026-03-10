class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_queue = deque()
        max_queue = deque()
        max_len = l = 0

        for r in range(len(nums)):
            while min_queue and min_queue[-1] > nums[r]:
                min_queue.pop()
            min_queue.append(nums[r])

            while max_queue and max_queue[-1] < nums[r]:
                max_queue.pop()
            max_queue.append(nums[r])

            while max_queue[0] - min_queue[0] > limit:
                if nums[l] == min_queue[0]:
                    min_queue.popleft()
                
                if nums[l] == max_queue[0]:
                    max_queue.popleft()
                l += 1

            max_len = max(max_len, r - l + 1)

        return max_len