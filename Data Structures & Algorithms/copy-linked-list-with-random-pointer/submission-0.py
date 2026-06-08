"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # we have to create a new linked list that looks exactly like the one given 
        # it would be simple to create if we could just go through the original 
        # and then for each node, create a new node that looks like it
        # the only problem is the random pointer that may point to a node that hasn't
        # been created yet
        # best thing is to store these values so we can just refer to them 
        # we set the key none to a none value to avoid the error when trying to access a node.random
        # key that is none
        old_to_new = {None: None}  
        curr = head
        # this first while loop just points the old node to its new node
        # it's also a good reference when trying to find the node.next and node.random vals for a new node
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next
        # here, we go through the old linked list and use its nodes as keys to search in the dictionary
        # for specific node that will be a .next or .random val for the new nodes
        curr = head 
        new_head = old_to_new[curr]
        while curr:
            # in this case we're not creating the new nodes but only accessing them since we already created them
            new_node = old_to_new[curr]
            # these give us actual nodes, not plain values in the old linked list
            new_node.next = old_to_new[curr.next] 
            new_node.random = old_to_new[curr.random]
            curr = curr.next

        return new_head
