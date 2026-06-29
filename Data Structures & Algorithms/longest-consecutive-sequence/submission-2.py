class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        x = set(nums)
        
        longest = 1
        length = 1

        for i in x:
            if i+1 not in x:
                num = i
                while num-1 in x:
                    length+=1
                    num -= 1
                else:
                    longest = max(length, longest)
            length = 1
        
        return max(length, longest)

