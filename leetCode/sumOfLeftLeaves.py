# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        stack = []
        sum = 0
        curr = root
        while True:
            if curr:
                stack.append(curr)
                if curr.left is not None and (curr.left.left is None and curr.left.right is None):
                    sum += curr.left.val
                curr = curr.left
            elif stack:
                curr = stack.pop()
                curr = curr.right
            
            else:
                break
        
        return sum
                
