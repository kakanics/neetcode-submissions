class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        symbols = []

        for i in tokens:
            if i != '+' and i != '-' and i != '*' and i != '/':
                nums.append(int(i))
            else:
                nums1, nums2 = nums.pop(), nums.pop()
                if i == "+":
                    nums.append(nums1+nums2)
                elif i == "-":
                    nums.append(nums2-nums1)
                elif i == "*":
                    nums.append(nums1*nums2)
                elif i == "/":
                    nums.append(int(nums2/nums1))

        return nums[-1]