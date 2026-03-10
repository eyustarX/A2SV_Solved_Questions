class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for i, n in enumerate(num):
            while k and stack and stack[-1] > n:
                stack.pop()
                k -= 1

            stack.append(n)
        
        while k:
            stack.pop()
            k -= 1

        ans = "".join(stack).lstrip('0')

        return ans if ans else '0'