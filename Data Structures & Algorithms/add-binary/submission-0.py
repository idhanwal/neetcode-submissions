class Solution:
    def addBinary(self, a: str, b: str) -> str:

        carry = 0

        i = len(a) - 1
        j = len(b) - 1
        res = ""
        while i >= 0 and j >= 0:
            total = int(a[i]) + int(b[j]) + carry
            carry = total // 2
            total = total % 2
            res = str(total) + res
            i -= 1
            j -= 1
        
        while i >= 0:
            total = int(a[i]) + carry
            carry = total // 2
            total = total % 2
            res = str(total) + res
            i -= 1
        
        while j >= 0:
            total = int(b[j]) + carry
            carry = total // 2
            total = total % 2
            res = str(total) + res
            j -= 1
        
        if carry:
            return "1" + res
        return res
        