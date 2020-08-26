def searchBST(root, key):
    if root is None:
        return 0
    if root.data == key:
        return 1

    if key < root.data:
        return searchBST(root.left, key)
    
    return searchBST(root.right, key)

def countPairs(root1, root2, x):
    stack = []
    curr = root1
    cnt = 0
    
    while True:
        if curr:
            stack.append(curr)
            curr = curr.left
        
        elif stack:
            curr = stack.pop()

            key = x - curr.data
            temp = root2
            
            if searchBST(temp, key):
                cnt += 1

            curr = curr.right
        
        else:
            break
    
    return cnt
    
#{ 
#  Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

def insert(root, node):
    if root == None:
        root = node
    else:
        if (root.data < node.data):
            if root.right == None:
                root.right = node
            else:
                insert(root.right, node)
        elif (root.data > node.data):
            if (root.left == None):
                root.left = node
            else:
                insert(root.left, node)
                
if __name__ == "__main__":
    t = int(input())
    while t>0:
        n1 = int(input())
        list = [int(x) for x in input().strip().split()]
        root1=Node(list[0])
        for i in range(1, n1):
            insert(root1, Node(list[i]))

        n2 = int(input())
        list = [int(x) for x in input().strip().split()]
        root2 = Node(list[0])
        for i in range(1, n2):
            insert(root2, Node(list[i]))
        s = int(input())
        print(countPairs(root1, root2, s))
        t=t-1