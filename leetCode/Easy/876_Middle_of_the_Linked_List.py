# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
Runtime 39ms, Faster than 63.73%
Memory Usage 13.8MB less than 71.92%
'''
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        answer = [head]
        
        while answer[-1].next:
            answer.append(answer[-1].next)
        
        return answer[len(answer)//2]