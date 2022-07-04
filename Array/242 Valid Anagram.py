class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        """
        # O(n)
        # Hashmap Solution using only 1 dict
        count = {}
        
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            count[s[i]] = 1 + count.get(s[i], 0)
            count[t[i]] = count.get(t[i], 0) - 1
            
        for n, c in count.items():
            if c != 0:
                return False
        return True
        """

        # O(n) time and O(1) space solution
        # Array Solution with ord()

        count = [0] * 26

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        for num in count:
            if num != 0:
                return False
        return True
