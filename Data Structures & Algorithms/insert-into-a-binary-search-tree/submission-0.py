# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # if empty root return Node(val)
        if not root:
            return TreeNode(val)

        # f(1.right)
        
        #traversal function
        def dfs(node):
            
            # compare val with the curr
            if val > node.val:
                if not node.right:
                    node.right = TreeNode(val)
                else:
                    dfs(node.right)

            else:
                if not node.left: 
                    node.left = TreeNode(val)
                else:
                    dfs(node.left)      

        dfs(root)
        return root

