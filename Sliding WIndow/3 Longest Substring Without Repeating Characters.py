def lengthOfLongestSubstring(s):
    l, r = 0, 1
    hashset = set()
    res = 0

    while r <= len(s):
        hashset.add(s[l])
        while r < len(s) and s[r] not in hashset:
            hashset.add(s[r])
            r += 1
        l += 1
        r = l + 1
        res = max(res, len(hashset))
        hashset.clear()

    return res

def main():
  print(lengthOfLongestSubstring("dvdf"))

main()