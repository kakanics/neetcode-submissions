from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        x = []
        for i in strs:
            a = Counter(i)
            for j in range(len(x)+1):
                if j == len(x):
                    x.append([i])
                    break
                if a == Counter(x[j][0]):
                    x[j].append(i)
                    break
        return x