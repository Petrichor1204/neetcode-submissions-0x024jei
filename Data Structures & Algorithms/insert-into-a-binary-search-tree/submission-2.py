# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
        U: insert a new value in a binary search tree
            I: root of bst - node, val - int
            O: root of bst - node
            C: work with negative vals or mix of neg and pos
            E: empty node - return None, neg insert into pos
            insert 9
            5
            /\
           3  6
            \  \
             4  10
                / \ 
               7  11
              --------
                \
                 9             
        M: dfs - recursion
        P: start at root, compare root val to value
            if value < root.val: go left
            else go right
            until at the leaf node
            plug as a node
        I:
        R:
        E:
        5.right = 6.right = 10.right = 7.right = 9
        """
        if not root:
            return TreeNode(val)

        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
            
        return root