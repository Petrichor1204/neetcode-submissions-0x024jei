class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # goal: return all the subsets in nums
        result = []

        def dfs(i, subset):
            # nums = [1,2,3]
            #             i
            #             j
            result.append(list(subset))

            # termination


            # continuation
            for j in range(i, len(nums)):
                subset.append(nums[j])
                dfs(j + 1, subset)
                subset.pop()


        dfs(0, [])
        return result
 
    # [[],[1],[1,2],[1,2,3],[2],[2,3],[3]]
    # dfs(0, []) 
    # dfs(1, [])
    # dfs(2, [])
        
       
            
        
           
            
                

