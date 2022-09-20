class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        x = 0
        curr_ave = 0.0
        max_ave = 0.0
        
        for i in range(len(nums)):
            if i < k:
                curr_ave += (nums[i] / k)
                max_ave = curr_ave
                continue
            else:
                curr_ave -= (nums[x] / k)
                curr_ave += (nums[i] / k)
                x += 1
            max_ave = max(curr_ave, max_ave)
            
        max_ave = max(curr_ave, max_ave)
            
        return max_ave
    
        '''
        Improved solution for readability and conciseness
        curr_ave = max_ave = sum(nums[:k]) / k
        
        for i in range(0, len(nums) - k):
            curr_ave += (nums[i + k] / k) - (nums[i] / k)  
            max_ave = max(curr_ave, max_ave)
            
        return max_ave
        '''