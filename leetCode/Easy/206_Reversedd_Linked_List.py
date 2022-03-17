# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
    :type head: ListNode
    :rtype: ListNode
"""
        
    
class Solution(object):
    def reverseList(self, head):
        node = head
        prev = None
        
        while node:
            node.next, next = prev, node.next
            prev, node = node, next
        return prev