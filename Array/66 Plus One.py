class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        number = 0
        for digit in digits:
            number = number * 10
            number = number + digit

        number += 1

        res = [int(x) for x in str(number)]

        return res
