# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # use slow and fast pointer to find the middle of the list
            # when the fast is at the end, the slow is at the middle
        # so at the end i know the fast pointer is at the end of the list
        # then i reverse from after the slow to the end
        # so now that is a separate linked list and ill keep track of 
        # the thing at the end as the head
        # then i traverse from that point while plugging in two steps
        # consider edge cases
        #             np
        # [2,4,6,10,8]
        #      s
        #        c
        #      
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        curr = slow.next
        slow.next = None

        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        curr = head
    
        while prev:
            np = prev.next
            nxt = curr.next
            curr.next = prev
            prev.next = nxt
            curr = nxt
            prev = np


        

