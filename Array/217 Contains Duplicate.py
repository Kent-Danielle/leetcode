class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Optimal solution v1.0 aka Hash Map Approach
        # O(n)
        # Iterate on the array
        # Save on the hash table 
        # Check if the next element exists in the hash table
        hashset = set()
        
        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False
        
        # Brute force
        # O(n^2)
        """
        length = len(nums)
        for i in range(length):
            for j in range(i + 1, length):
                if nums[i] == nums[j]:
                    return True
        return False
        """
            