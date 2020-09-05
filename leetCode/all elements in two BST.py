# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        stack = []
        values = []
        
        curr = root1
        while True:
            if curr:
                stack.append(curr)
                curr = curr.left
            
            elif stack:
                curr = stack.pop()
                values.append(curr.val)
                curr = curr.right
            
            else:
                break
        
        curr = root2
        while True:
            if curr:
                stack.append(curr)
                curr = curr.left
            
            elif stack:
                curr = stack.pop()
                values.append(curr.val)
                curr = curr.right
            
            else:
                break
        
        return sorted(values)
