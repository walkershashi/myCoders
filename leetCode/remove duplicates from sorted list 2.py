# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        
        cntr = {}
        temp = head
        while temp:
            try:
                cntr[temp.val] += 1
            except:
                cntr[temp.val] = 1
            
            temp = temp.next
        
        temp_head, temp_tail = None, None
        
        for val, cnt in cntr.items():
            if cnt == 1:
                if temp_head is None:
                    temp_head = ListNode(val)
                    temp_tail = temp_head
                
                else:
                    temp_tail.next = ListNode(val)
                    temp_tail = temp_tail.next
        
        return temp_head
