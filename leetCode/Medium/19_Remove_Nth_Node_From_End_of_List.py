# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
    :type head: ListNode
    :type n: int
    :rtype: ListNode
"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def removeNthFromEnd(self, head, n):
       
        dummy = ListNode(0)
        dummy.next = head
        
        prev_node = next_node = dummy
        
        for i in range(n):
            next_node = next_node.next
        
        while next_node.next :
            prev_node = prev_node.next
            next_node = next_node.next
        
        prev_node.next = prev_node.next.next
        
        return dummy.next
