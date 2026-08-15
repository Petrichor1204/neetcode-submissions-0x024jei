# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        # removing the node with the given key from the tree
        # searching for the node to remove
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)

        # if node is found, delete - root.val == key.val
        # take the smallest value in the right subtree
        else:  
            if not root.left:
                return root.right
            if not root.right:
                return root.left
                
            curr = root.right
            while curr.left:
                curr = curr.left

            # curr is last left node
            root.val = curr.val

            # delete the node we copied
            root.right = self.deleteNode(root.right, curr.val)

        return root


        
        