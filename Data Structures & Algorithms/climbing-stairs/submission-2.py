class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [-1] * (n + 1)
        count = 0
        # dfs(3) dfs(2) dfs(1) dfs(0)
        def dfs(n):
            nonlocal count
            if n == 0:
                return 1

            if n < 0:
                return 0

            if memo[n] != -1:
                return memo[n]

            memo[n] = dfs(n - 1) + dfs(n - 2)
            return memo[n]
            
    
        dfs(n)
        return memo[n]
        
