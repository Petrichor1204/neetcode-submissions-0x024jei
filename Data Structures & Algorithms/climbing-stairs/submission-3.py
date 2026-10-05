class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        # [0,1,-1]
        # number of ways up to n - 1 + ways up to n - 2
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]
            
            
        
