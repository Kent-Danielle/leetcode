class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # Find a unique element
            # Of course, the first one would always be unique
        # then look at the next element
            # If it's a duplicate then we remove it and just loop this until it's a unique one
        
        # Have a pointer:
        # A second pointer is not necessary as it is always i + 1
        x = 1
        
        # Use a while loop instead of a for loop because the size of the array is always changing
        for i in range(len(nums) - 1):
            # Check if the element at the right is a duplicate of the current element
            if nums[i] != nums[i + 1]:
                # If it's not a duplicate then, we move the element on the right of the duplicate on its place
                nums[x] = nums[i + 1]
                # Increment x because we're sure that nums[i] and nums[i + 1] (where x = i + 1) is always unique
                x += 1
        return x
    
        # Time Complexity = O(n)
        # Time Complexity = O(1)
        