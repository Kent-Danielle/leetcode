class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Brute force solution
        # O(n^2)
        
        # Iterate every element in the array
        # Subtract it from the target
        # Find the difference in the remaining element
        # Repeat until the end
        '''
        for i in range(len(nums)):
            num = target - nums[i]
            if num in nums[i + 1:]:
                return [i, nums.index(num, i + 1)]
        '''
        
        # Better solution
        # O(n)
        
        # Have an empty dictionary
        # Key = integer, Value = index
        prevMap = {}
        
        # Use enumerate function to get the index and the value
        for i, n in enumerate(nums):
            # Similar strategy to Brute force
            diff = target - n
            if diff in prevMap:
                # Now, we search inside a hashmap which is O(1) instead of an O(n) in an array
                # If we find it, we can return the current index
                # and also look at the dict using the diff as the key which returns the index
                return [prevMap[diff], i]
            # If it doesn't exist yet, then just save it on the dict
            # by using the value as the key, and the index as the value
            prevMap[n] = i