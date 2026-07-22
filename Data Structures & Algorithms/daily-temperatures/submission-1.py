class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        max = [0] * len(temperatures)
        stack = [(temperatures[-1], len(temperatures)-1)]

        for i in range(len(temperatures)-2, -1, -1):
            if temperatures[i] >= stack[-1][0]:
                while len(stack) and temperatures[i] >= stack[-1][0]:
                    stack.pop()
                if len(stack):
                    max[i] = stack[-1][1] - i
                stack.append((temperatures[i], i))
            else:
                max[i] = stack[-1][1] - i
                stack.append((temperatures[i], i))

        return max