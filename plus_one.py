# leetcode
class Solution:
    def plusOne(self, digits):
        carry = 0
        for i in reversed(range(len(digits))):
            if i == len(digits) - 1:
                current_sum = digits[i] + carry + 1
            else:
                current_sum = digits[i] + carry
            carry = 1 if current_sum > 9 else 0
            current_sum %= 10
            digits[i] = current_sum
        if carry == 1:
            digits.insert(0,1)
        return digits

s = Solution()
print(s.plusOne([99]))