class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # goal: is to take a list of operations, perform the operations and then return 
        # the sum of the result list
        #  ops=["5","-2","4","C","D","9","+","+"]
        #                                     i
        # [5,-2,4,9,13]
        stack = []
        for char in operations:
            # if char is num, add to stack
            if char not in "CD+":
                stack.append(int(char))
            # if char is plus, add prev two
            elif len(stack) > 1 and char == "+":
                stack.append((stack[-1] + stack[-2]))
            # if char is a D, take last thing and * 2
            elif stack and char == "D":
                stack.append((stack[-1] * 2))
            # if char is C, pop last thing in stack
            elif stack and char == "C":
                stack.pop()


        # return sum of result
        return sum(stack)