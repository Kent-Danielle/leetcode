class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        length = 0
        
        while i >= 0 and s[i] == " ":
            i -= 1
        
        for j in range(i, -1, -1):
            if s[j] == " ":
                break
            length += 1
        
        return length
        