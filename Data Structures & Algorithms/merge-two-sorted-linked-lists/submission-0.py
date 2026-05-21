# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # list1 = [1,2,4], list2 = [1,3,5]
        #                a
        #                               b
        # dummy -> 1 -> 1 -> 2 -> 3 -> 4 ->
        # 
        if not list1:
            return list2
        elif not list2:
            return list1
        
        



        a = list1
        b = list2
        dummy = ListNode()

        if a.val <= b.val:
            dummy.next = a
            a = a.next
        else:
            dummy.next = b
            b = b.next

        curr = dummy.next

        while a and b:
            if a.val <= b.val:
                curr.next = a
                curr = curr.next
                a = a.next
            else:
                curr.next = b
                curr = curr.next
                b = b.next
        # the last thing we added to the new list is what doesnt exist anymore
        # so we traverse through the other list
        # curr = other pointer
        if b:
            curr.next = b
        else:
            curr.next = a
        return dummy.next
            
         
        
