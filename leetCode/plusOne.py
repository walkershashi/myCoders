class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        else:
            carry = 1
            for i in range(len(digits)):
                sum = digits[len(digits) -1 - i] + carry
                digits[len(digits) - 1 - i] = sum % 10
                carry = sum // 10
            
            if carry == 1:
                digits.insert(0, carry)
            return digits
