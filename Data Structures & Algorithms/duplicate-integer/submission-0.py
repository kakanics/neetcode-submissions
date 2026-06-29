class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        x = set()
        for i in nums:
            x.add(i)
        return len(nums) != len(x)