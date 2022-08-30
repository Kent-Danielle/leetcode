class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = x
        y = 0
        
        while temp >= 0:
            y = y + (temp % 10)
            temp = temp // 10
            if temp <= 0:
                return x == y
            y = y * 10
        
        