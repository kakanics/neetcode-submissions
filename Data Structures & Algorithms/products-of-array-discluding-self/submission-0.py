class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count_zero = 0
        product = 1
        for i in nums:
            if i == 0:
                count_zero += 1
            else:
                product *= i
        
        ans = []
        for i in nums:
            if count_zero == 0:
                ans.append(product//i)
            elif count_zero == 1:
                if i == 0:
                    ans.append(product)
                else:
                    ans.append(0)
            else:
                ans.append(0)
        
        return ans
