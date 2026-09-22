# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_digits, l2_digits = [], []
        # traverse first add to list
        while l1:
            l1_digits.append(str(l1.val))
            l1 = l1.next

        # traverse second add to list
        while l2:
            l2_digits.append(str(l2.val))
            l2 = l2.next

        # get both numbers and add up and put result in list
        num1 = int("".join(reversed(l1_digits)))
        num2 = int("".join(reversed(l2_digits)))

        total = num1 + num2

        total_list = [int(s) for s in str(total)]

        # traverse result and add digits to ll
        dummy = ListNode()
        curr = dummy
        for num in reversed(total_list):
            curr.next = ListNode(num)
            curr = curr.next

        return dummy.next
