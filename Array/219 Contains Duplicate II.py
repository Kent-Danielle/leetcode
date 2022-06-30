def containsNearbyDuplicate(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    hashmap = {}
    
    for i, num in enumerate(nums):
        if num in hashmap and abs(i - hashmap[num]) <= k:
            return True
        hashmap[num] = i
    return False