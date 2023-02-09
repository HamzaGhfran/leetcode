class Solution:
    def isPalindrome(self, x: int) -> bool:
        reminder = 0
        a = x
        if x < 0:
            return False
        while x > 0:
            reminder = reminder * 10 + x % 10
            
            x = int(x / 10)
        if reminder == a:
            return True