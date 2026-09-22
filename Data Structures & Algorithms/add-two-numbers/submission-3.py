# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        rem = 0
        # 1 -> 2
        # 9
        #      l2
        # dummy -> 0 -> 3
        #               c        
        # go node by node for each at the same time and add them up
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            curr_sum = (val1 + val2 + rem) % 10
            rem = (val1 + val2 + rem) // 10
            curr.next = ListNode(curr_sum)
            curr = curr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        #  if there's extra digits
        # if there's a remainder left
        if rem > 0:
            curr.next = ListNode(rem)
       
        
        

        return dummy.next
        