# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # the n cannot be greater than number of nodes
        # we will be given an n and we have to remove the nth node counting from the end
        # add dummy to head
        # [1,2,3,4] n = 2
        # create a regular list 
        # put nodes in that list
        # find the node at position n counting from the back
        # unplug that node from linked list and reconnect the pointers
        # return the original linked list
        # d -> 1 -> 2 -> 3 -> 4 ->
        #      p      
        #           c         
        #           
        
        dummy = ListNode(0)
        dummy.next = head
        nodes = []
        # traversing linked list
        curr = dummy.next
        while curr:
            nodes.append(curr)
            curr = curr.next
        # nodes = [1,2,3,4]
        # find node in linked list and unplug
        # loop through nodes backwards n times
        node = nodes[len(nodes)-n]

        # start at the head of ll
        prev = dummy 
        curr = dummy.next
        while curr:
            temp = curr.next
            if curr == node:
                # remove it
                prev.next = temp
            # if not, just continue
            prev = curr
            curr = temp
        return dummy.next
            




        
