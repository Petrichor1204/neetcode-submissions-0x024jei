class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens:
            return 0
        # ["1","2","+","3","*","4","-"]
        # [3,9,4,5] res = op2 + op1
        # use a stack to reverse the order to operations before numbers
        stack = []
        # add to stack until you see operation
        # operation is actually for only two most recent numbers
        # for division and subtraction, order matters
        # how do we flip direction of number to perform operation?
        for char in tokens:
            if char in "+-*/":
                op1 = stack.pop()
                op2 = stack.pop()
                if char == "+":
                    res = op2 + op1
                    stack.append(res)
                elif char == "-":
                    res = op2 - op1
                    stack.append(res)
                elif char == "*":
                    res = op2 * op1
                    stack.append(res)
                elif char == "/":
                    res = int(op2 / op1)
                    stack.append(res)
            else:
                stack.append(int(char))
        # return the last thing in the stack after end of iteration
        return stack.pop()
      

