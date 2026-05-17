# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # <- 0 <- 1 <- 2 <- 3 
        #                   p 
        #                     c
        #                     
        # we want to set the next pointer to the previous node
        # so take curr pointer, set it to prev node
        # when we turn curr from its next pointer, we forget what we were pointing
        # to and so can't find it when we're trying to work with that
        # so we put a temporary tracker on it

        if not head:
            return None

        prev = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev


