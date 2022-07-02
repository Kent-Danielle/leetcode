class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        """
        # O(n)
        for i in range(len(nums)):
            if target <= nums[i]:
                return i
        return i + 1
        """
        # O(logn)
        # Use iterative binary search to keep track of the left
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left
