def sortedInsert(head, data):
    temp = DoublyLinkedListNode(data)
    head_ref = head

    if head_ref is None:
        head_ref = head

    elif data <= head_ref.data:
        temp.next = head_ref
        head_ref.prev = temp
        head = temp

    else:
        while head_ref.next and data > head_ref.next.data :
            head_ref = head_ref.next
        
        temp.next = head_ref.next

        if head_ref.next is not None:
            head_ref.next.prev = temp
        
        head_ref.next = temp
        temp.prev = head_ref

    return head
