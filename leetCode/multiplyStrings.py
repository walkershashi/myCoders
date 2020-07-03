class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num_1 = 0
        num_2 = 0
        
        str_num = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        num_str = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}
        
        for i in num1:
            num = str_num[i]
            num_1 = num_1 * 10 + num
        
        for i in num2:
            num = str_num[i]
            num_2 = num_2 * 10 + num
            
        prod = num_1 * num_2
        
        str_prod = ''
        
        if prod == 0:
            return '0'
        
        while prod > 0:
            last_num = prod - (prod//10)*10
            
            str_prod += num_str[prod % 10]
            prod //= 10
            
        
        return str_prod[::-1]
