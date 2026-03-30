class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i, n in enumerate(temperatures):
            while stack and n > temperatures[stack[-1]]:
                curr = stack.pop()
                result[curr] = i - curr
            stack.append(i)

            
        return result

