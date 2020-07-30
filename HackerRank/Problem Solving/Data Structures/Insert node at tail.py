def insertNodeAtTail(head, data):
    temp = SinglyLinkedListNode(data)

    if head is None:
        head = temp

    else:
        head_ref = head

        while head_ref.next:
            head_ref = head_ref.next
    

        head_ref.next = temp

    return head