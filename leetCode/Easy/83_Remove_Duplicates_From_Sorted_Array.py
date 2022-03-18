# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head 
        
        while current.next :
            if current.next and current.val == current.next.val :
                current.next == current.next.next
            else :
                current = current.next
            
        print(head)
        return head 