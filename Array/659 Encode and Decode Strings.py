class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """

    def encode(self, strs):
        # write your code here
        res = ""
        for s in strs:
            res += len(s) + "#" + s

        return res

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """

    def decode(self, str):
        # write your code here
        strs, i = [], 0

        while i < len(strs):
            j = i
            while j != "#":
                j += 1

            length = int(str[i:j])
            strs.append(str[j + 1: j + 1 + length])
            i = j + 1 + length
        return strs
