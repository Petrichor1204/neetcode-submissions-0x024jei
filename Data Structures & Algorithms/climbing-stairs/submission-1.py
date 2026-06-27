class Solution:
    def climbStairs(self, n: int) -> int:
        def f(n, memo):
            if n == 0:
                return 1
            if n < 0:
                return 0
            if memo[n] != -1:
                return memo[n]

            left = f(n - 1, memo)
            right = f(n - 2, memo)

            memo[n] = left + right
            return memo[n]
      
            
        memo = [-1] * (n + 1)
        return f(n, memo)
        
