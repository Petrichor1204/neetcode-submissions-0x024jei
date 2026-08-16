class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # find all k possible combinations of n numbers
        # [1,2,3]
       
        result = []
        def dfs(i, subset):
            # termination
            if len(subset) == k:
                result.append(list(subset))
                

            # continuation
            for j in range(i, n): 
                subset.append(j+1)
                dfs(j + 1, subset)
                subset.pop()


        dfs(0, [])
        return result
    # i = 1, j = 1
    # dfs(0, [1]) dfs(1, [1,2]) dfs(2, [1,2,3])
    # [[1,2],]