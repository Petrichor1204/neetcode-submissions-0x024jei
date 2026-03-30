class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(s, opened, closed):
            if len(s) == n * 2:
                res.append(s)
                return
                

            if opened < n:
                backtrack(s + "(", opened+1, closed)
               
            if closed < opened:
                backtrack(s + ")", opened, closed+1)
               
        backtrack("", 0, 0)
        return res