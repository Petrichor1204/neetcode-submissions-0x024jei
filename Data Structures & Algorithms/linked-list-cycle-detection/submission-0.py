# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # return true if there is a cycle, else return false
        # 1 -> 2 -> 3 -> 4 -> connect to 2
        # s 
        # f 
        # 1 ->
        # s
        # f
        # move slow by one step at a time, fast by two steps at a time
        # at each point, we check if they are at the same node, 
            # if so return true, else return false
        # we will be traversing until we get to the end of the list
        # or until we return true that is, we see a cycle
        # if we are at then end of the list and we havent returned true 
            # then we return false
        # set slow and fast to head 
        # if only one element, return false
        if not head:
            return False

        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


