class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        
        l = 0
        res = list(s)
        r = len(res) - 1
        while l <= r:
            while l <= r and res[l] not in vowels:
                l += 1
            while l <= r and res[r] not in vowels:
                r -= 1
            
            if l <= r and res[l] in vowels and res[r] in vowels:
                res[l], res[r] = res[r], res[l]
            l += 1
            r -= 1

        return ''.join(res)
        