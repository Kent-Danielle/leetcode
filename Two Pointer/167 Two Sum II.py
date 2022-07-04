class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        # Stupid O nlogn Solution
        for i in range(len(numbers)):
            diff = target - numbers[i]
            j = self.binarySearch(numbers, i, diff)
            if j != None:
                return [i + 1, j + 1]
        """
        # Chad  O n Solution
        start, end = 0, len(numbers) - 1
    
        while start < end:
            currSum = numbers[start] + numbers[end]

            if currSum > target:
                end -= 1
            elif currSum < target:
                start += 1
            else:
                return [start + 1, end + 1]
    """
    def binarySearch(self, arr, i, target):
        start, end = i + 1, len(arr) - 1
    
        while start <= end:
            mid = (start + end) // 2

            if arr[mid] == target:
                return mid

            if arr[mid] > target:
                end = mid - 1
            elif arr[mid] < target:
                start = mid + 1
        return None
    """