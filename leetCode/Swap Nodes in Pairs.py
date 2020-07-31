def swapPairs(self, head: ListNode) -> ListNode:
	# Given: 1 -> 2 -> 3 -> 4 -> NULL
	# O/P:   2 -> 1 -> 4 -> 3 -> NULL
        if head is None or head.next is None:
            return head
        else:
            href = head
            h_ref = head.next
        
            while h_ref:
                href.val, h_ref.val = h_ref.val, href.val
                href = href.next.next
                if h_ref.next is not None:
                    h_ref = h_ref.next.next
                else:
                    h_ref = h_ref.next
            
        return head
