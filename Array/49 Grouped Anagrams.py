def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    grouped = [[]]
    i = 0
    j = 0
    while len(strs) - 1 > 0:
        if isAnagram(strs[i], strs[i + 1]):
            grouped[j].append(strs[i + 1])
            del strs[i + 1]
            continue
        grouped[j].append(strs[i])
        del strs[i]
        i += 1
        j += 1
    return grouped
            
        
def isAnagram(s, t):
    countS, countT = {}, {}
    
    if len(s) != len(t):
        return False
    
    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
    
    for c in countS:
        if countS[c] != countT.get(c, 0):
            return False
    
    return True    

def main():
    print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
    
main()