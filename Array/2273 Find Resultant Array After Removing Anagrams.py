class Solution(object):
    def removeAnagrams(self, words):
        i = 0
        while i < len(words) - 1:
            if self.isAnagram(words[i], words[i + 1]):
                words.remove(words[i + 1])
                continue
            i += 1
        return words
        
    def isAnagram(self, s, t):
        countS, countT = {}, {}
        
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        
        return True
        