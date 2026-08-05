# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # find the subtree in root that has subroot's structure and node values
        # 1. search the right and left halves
        if not root:
            return False

        # 2. compare similar subtrees
        def isSameTree(root, subRoot):
            if not root and not subRoot:
                return True

            if not root or not subRoot:
                return False

            if root.val == subRoot.val:
                return isSameTree(root.left, subRoot.left) and isSameTree(root.right, subRoot.right)
            return False

        if isSameTree(root, subRoot):
            return True

        # search left
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


        
       

 
