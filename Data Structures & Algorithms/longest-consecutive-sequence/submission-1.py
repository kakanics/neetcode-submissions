class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        nums.sort()


        longest = 0
        length = 0

        print(nums)

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            if nums[i] > nums[i-1]+1:
                longest = max(length, longest)
                length = 0
            else: 
                length += 1

        return max(length+1,longest+1)
