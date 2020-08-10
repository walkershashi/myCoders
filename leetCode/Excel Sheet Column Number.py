class Solution:
    def titleToNumber(self, s: str) -> int:
        alpha = {'A': 1, 'C': 3, 'B': 2, 'E': 5, 'D': 4, 'G': 7, 'F': 6, 'I': 9, 'H': 8, 'K': 11, 'J': 10, 'M': 13, 'L': 12, 'O': 15, 'N': 14, 'Q': 17, 'P': 16, 'S': 19, 'R': 18, 'U': 21, 'T': 20, 'W': 23, 'V': 22, 'Y': 25, 'X': 24, 'Z': 26}
        
        index = 0
        for i in range(1, len(s) + 1):
            index += alpha[s[i-1]] * 26**(len(s)-i)
            
        return index
        
