class Solution:
    def reverse(self, x: int) -> int:
        
        rev_x = ''
        if x < 0:
            
            x = str(x)[1:]
            x = x[::-1]
            rev_x =  '-' + x
        else:
            x = str(x)
            x = x[::-1]
            rev_x = x
        
        MIN = -2**31
        MAX = 2**31 - 1
        if int(rev_x) < MIN or int(rev_x) > MAX:
            return 0
        else:
            return int(rev_x)
