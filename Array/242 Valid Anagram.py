class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Have two dicts to keep track of each character
        hashmapS, hashmapT = {}, {}
        
        # If the two strings doesn't have equal num of characters, then it's not an anagram
        if len(s) != len(t):
            return False
        
        # Iterate through each of the characters 
        for i in range(len(s)):
            # Make a key for each character
            # Use get() to increment if the key already exists, or set to (1 + 0) if it doesn't
            hashmapS[s[i]] = 1 + hashmapS.get(s[i], 0)
            hashmapT[t[i]] = 1 + hashmapT.get(t[i], 0)

        # Check all of the keys of a dict and compare it to the other
        # If one of them aren't equal then it's not an anagram
        # get() is used in case there's a character in one string that doesn't exist on the other string
        for c in hashmapS:
            if hashmapS[c] != hashmapT.get(c, 0):
                return False
            
        return True