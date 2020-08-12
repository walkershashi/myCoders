""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
def check_binary_search_tree_(root):
    stack = []
    values = []
    curr = root
    
    while True:
        if curr:
            stack.append(curr)
            curr = curr.left
        
        elif stack:
            curr = stack.pop()
            values.append(curr.data)
            curr = curr.right
        
        else:
            break
    #print(values)
    sort_values = list(set(sorted(values)))
    #print(sort_values)
    if sort_values == values:
        return 1
    else:
        return 0
