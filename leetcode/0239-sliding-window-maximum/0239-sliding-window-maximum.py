class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        ans = []
        max_num = nums[0]

        for i in range(len(nums)):
            while   queue and   queue[-1] < nums[i]:
                queue.pop()

            queue.append(nums[i])

            if i >= k and nums[i - k] == queue[0]:
                queue.popleft()

            if i + 1 >= k:
                ans.append(queue[0])

        return ans