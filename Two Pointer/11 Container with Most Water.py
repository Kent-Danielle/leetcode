def maxArea(height):
    res = 0 
    left, right = 0, len(height) - 1
    
    while left < right:
        # Compare the old and new res value where
        # new res = (right - left) * min(height[left], height[right])
        res = max((right - left) * min(height[left], height[right]), res)
        
        # Move the pointers left to right and right to left
        if height[left] < height[right]:
            left += 1
        elif height[right] <= height[left]:
            right -= 1
            
    return res


def main():
  print(maxArea([1,8,6,2,5,4,8,3,7]))
  
main()