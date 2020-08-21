# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return 
        
        values = []
        temp = head
        
        while temp:
            values.append(temp.val)
            temp = temp.next
        
        temp = head
        i = 0
        j = len(values) - 1
        while temp and temp.next:
            temp.val = values[i]
            temp.next.val = values[j - i]
            
            i += 1
            
            if temp.next is None:
                temp.next = None
                temp = temp.next
            
            else:
                temp = temp.next.next
        
        if len(values)%2 != 0:
            temp.val = values[len(values)//2]
        
