# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # [2,4,6,8]
        # [2,8,4,6,8]
        #      c               
        #        t
        # we can put the nodes in a list with each index representing their positions
        # first traverse the list to put each node in a new list
        # create a list
        nodes = []
        # traversing the list
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next

        # reordering

        curr = head
        for i in range(len(nodes)//2):
            node = nodes.pop()
            temp = curr.next
            curr.next = node
            node.next = temp
            curr = temp
            
        curr.next = None
        



