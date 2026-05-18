class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # [30,38,30,36,35,40,28]
        # [1, 4, 1, 2, 1, 0, 0]
        # what do we need = array of days where each day represents how many 
        # days after that day where it took to get a warmer temperature
        # while curr > last thing in stack: pop last thing
        # when i pop, calc bigger_index - smaller_index 
        # update result with calc
        # compare before you pop

        # stack = [38]
        # result = [1,4,1,2,1,0,0]
        stack = [] #indexes
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            # if stack is not empty and temp > last thing in stack 
            while stack and temperatures[i] > temperatures[stack[-1]]:
                # update result with diff bigger temp and smaller temp
                res[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return res
           
