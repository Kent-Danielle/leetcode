class Solution:
    def romanToInt(self, s: str) -> int:
        
        hashMap = {"I": 1,"IV": 4, "V": 5,"IX":9, "X": 10,"XL":40, "L": 50,"XC":90, "C": 100,"CD":400, "D": 500,"CM":900, "M": 1000}
        
        res = 0
        left, right = 0, 1
        
        length = len(s)
        if length == 1:
            return hashMap[s]
        
        while right < length:
            if hashMap.get(s[left] + s[right]) != None:
                res += hashMap[s[left] + s[right]]
                left += 2
            else:
                res += hashMap[s[left]]
                left += 1
            right = left + 1
            
        if left < length:
            res += hashMap[s[left]]
        
        return res