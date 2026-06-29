class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        x = {}
        for i in nums:
            x[i]=x.get(i,0)+1
        lst = []
        for i in x:
            lst.append([x[i], i])

        lst.sort()
        l = []
        for q in range(len(lst)-1, len(lst)-1-k, -1):
            l.append(lst[q][1])
        return l