class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # [30,38,30,36,35,40,28]
        #                 i                     
        #                  
        # [(38,1),(36,3)]
        # [1,0,1,0,1,0,0]
        # res[i] = j - i => o(n)^2
        # condition to add to stack = each val we encounter
        # condition to remove from stack = if curr val is bigger than stack[-1]
        # initialize results with zeros
        # need a way to keep track of indexes - tuple of val,index in stack
        # while curr val is bigger than last thing in stack:
            # pop from stack and update results

        results = [0 for _ in range(len(temperatures))]
        # put first val, index in stack
        stack = [0]

        for i in range(1, len(temperatures)):
            # if stack is not empty
            if stack:
                while stack and temperatures[i] > temperatures[stack[-1]]:
                    results[stack[-1]] = i - stack[-1]
                    stack.pop()
                stack.append(i)
        return results


