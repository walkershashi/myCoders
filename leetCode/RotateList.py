# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None or head.next is None:
            return head
        
        href = head
        cnt = 0
        while href:
            cnt += 1
            href = href.next
        
        if k%cnt == 0:
            return head
        else:
            for i in range(k%cnt):
                first = head
                second = head.next
                
                while second.next:
                    first = first.next
                    second = second.next

                second.next = head
                first.next = None
                head = second

            return head
