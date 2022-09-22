from re import S


def compressString(s):
  length = len(s)
  if length <= 2:
    return s
  
  l = 0
  r = 1
  en_str = ""
  
  while r < length:
    while r < length and s[l] == s[r]:
      r += 1
    
    en_str += s[l] + (str) (r - l)
    l = r
    r = l + 1
  
  return en_str if len(en_str) < length else s
  

def main():
  print(compressString("aabcccccaaa"))

main()