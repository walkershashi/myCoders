class Solution:
    def toGoatLatin(self, S: str) -> str:
        if not S:
            return
        
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        S = S.split()
        for i in range(1, len(S)+1):
            if S[i-1][0] in vowels:
                S[i-1] += 'ma' + 'a'*i
            
            else:
                S[i-1] = S[i-1][1:] + S[i-1][0] + 'ma' + 'a'*i
        
        return ' '.join(i for i in S)
