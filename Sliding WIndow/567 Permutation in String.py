def checkInclusion(s1, s2):
    countS1 = {}
    for c in s1:
        countS1.update({c: 1 + countS1.get(c, 0)})

    countS2 = {}
    for i in range(len(s1)):
        countS2.update({s2[i]: 1 + countS2.get(s2[i], 0)})
    if countS1 == countS2:
        return True

    start = 0
    for i in range(len(s1), len(s2)):
        countS2.update({s2[i]: 1 + countS2.get(s2[i], 0)})

        if countS2.get(s2[start], 0) > 1:
            countS2.update({s2[start]: countS2.get(s2[start]) - 1})
        else:
            countS2.pop(s2[start])
        start += 1

        if countS1 == countS2:
            return True

    return False

print(checkInclusion("adc", "dcda"))