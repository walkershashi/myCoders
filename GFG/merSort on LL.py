#User function Template for python3

def getMid(temp):
    first = second = temp
    
    while first.next and first.next.next:
        second = second.next
        first = first.next.next
    
    return second

def Merger(head1, head2):
    if head1 is None:
        return head2
    
    if head2 is None:
        return head1
    
    res = None
    
    if head1.data <= head2.data:
        res = head1
        res.next = Merger(head1.next, head2)
    
    if head2.data < head1.data:
        res = head2
        res.next = Merger(head1, head2.next)
    
    return res

def mergeSort(head):
    '''
    :param head: head of unsorted linked list 
    :return: head of sorted linkd list
    
    # Node Class
    class Node:
        def __init__(self, data):  # data -> value stored in node
            self.data = data
            self.next = None
    '''
    if head is None or head.next is None:
        return head
    
    mid = getMid(head)
    nextMid = mid.next
    mid.next = None
    
    left = mergeSort(head)
    right = mergeSort(nextMid)
    
    sortedHead = Merger(left, right)
    
    return sortedHead
