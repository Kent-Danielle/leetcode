class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        htable = {}

        for num in nums:
            htable[num] = 1 + htable.get(num, 0)

        freq_arr = [[] for i in range(len(nums) + 1)]

        for num, freq in htable.items():
            freq_arr[freq].append(num)

        res = []
        for i in range(len(freq_arr) - 1, 0, -1):
            for num in freq_arr[i]:
                res.append(num)
                if len(res) == k:
                    return res
