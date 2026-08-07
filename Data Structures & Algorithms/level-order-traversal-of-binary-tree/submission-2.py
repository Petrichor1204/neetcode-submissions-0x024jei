# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # check if there is a node/nodes
        # create a sublist
        # add node/nodes to sublist
        # keep index for that node level
        # [[1],[2,3],[4,5,6,7]] 
        result = []
        def dfs(node, index):
            if not node:
                return
            
            # add sublist to result
            if len(result) == index:
                result.append([])

            
            dfs(node.left, index + 1) 
            dfs(node.right, index + 1)

            # append node to sublist at index
            result[index].append(node.val)

        dfs(root, 0)
        return result

