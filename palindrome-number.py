class Solution:
    def isPalindrome(self, x: int) -> bool:
        num=str(x)
        num2=num[::-1]
        if num==num2:
            return True
        else:
            return False
